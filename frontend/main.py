"""FastAPI proxy for Milan & Mandap on Agent Runtime (A2A 1.0 protocol).

The browser talks ONLY to this proxy (same origin, no CORS, no GCP creds in browser).
The proxy authenticates with ADC and forwards chat to the deployed agent over A2A.
"""

import json
import os
import re
import uuid

import google.auth
import google.auth.transport.requests
import httpx
from google.agents.cli.run.cmd_run import (
    ClientConfig,
    create_client,
    TransportProtocol,
    VERSION_HEADER,
    PROTOCOL_VERSION_1_0,
)
from a2a.types import Message, Part, Role, SendMessageRequest
from google.protobuf.json_format import MessageToDict
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

RESOURCE = os.environ.get(
    "AGENT_ENGINE_RESOURCE_NAME",
    "projects/661163409185/locations/us-central1/reasoningEngines/5559350142605197312",
)
AGENT_DIRECTORY = os.environ.get("AGENT_DIRECTORY", "milan_and_mandap_app")
LOCATION = RESOURCE.split("/locations/")[1].split("/")[0]

A2A_BASE = (
    f"https://{LOCATION}-aiplatform.googleapis.com/reasoningEngines/v1/"
    f"{RESOURCE}/api/a2a/{AGENT_DIRECTORY}"
)
A2A_CARD_URL = f"{A2A_BASE}/.well-known/agent-card.json"

app = FastAPI(title="Milan & Mandap Proxy")

_credentials, _ = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)


def _auth_headers() -> dict[str, str]:
    req = google.auth.transport.requests.Request()
    _credentials.refresh(req)
    return {"Authorization": f"Bearer {_credentials.token}"}


_contexts: dict[str, str] = {}


def _extract_parts(part: Part) -> list[dict]:
    out = []
    if part.text:
        text = part.text
        # Check if text contains raw A2UI payload or a2a_datapart_json tags
        if "<a2a_datapart_json>" in text or "<a2ui-json>" in text or '"surfaceUpdate"' in text:
            clean = re.sub(r"</?(?:a2a_datapart_json|a2ui-json)>", "", text).strip()
            try:
                data = json.loads(clean)
                if isinstance(data, dict):
                    # Could be wrapped in kind/data/metadata
                    payload = data.get("data", data)
                    out.append({"kind": "a2ui", "data": payload})
                    return out
            except Exception:
                pass
        out.append({"kind": "text", "text": text})
    elif part.HasField("data"):
        data_dict = MessageToDict(part.data)
        out.append({"kind": "a2ui", "data": data_dict})
    elif part.url:
        out.append({"kind": "text", "text": part.url})
    return out


@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    message = body.get("message", "")
    user_id = body.get("user_id") or "web-user"
    parts: list[dict] = []

    req_headers = _auth_headers()
    req_headers.setdefault(VERSION_HEADER, PROTOCOL_VERSION_1_0)

    async with httpx.AsyncClient(headers=req_headers, timeout=120) as http_client:
        config = ClientConfig(
            httpx_client=http_client,
            supported_protocol_bindings=[
                TransportProtocol.JSONRPC,
                TransportProtocol.HTTP_JSON,
            ],
        )
        a2a_client = await create_client(A2A_BASE, config)

        msg = Message(
            message_id=str(uuid.uuid4()),
            role=Role.ROLE_USER,
            parts=[Part(text=message)],
            context_id=_contexts.get(user_id, ""),
        )

        async for chunk in a2a_client.send_message(SendMessageRequest(message=msg)):
            if chunk.HasField("artifact_update"):
                if chunk.artifact_update.context_id:
                    _contexts[user_id] = chunk.artifact_update.context_id
                for p in chunk.artifact_update.artifact.parts:
                    parts.extend(_extract_parts(p))
            elif chunk.HasField("task"):
                if chunk.task.context_id:
                    _contexts[user_id] = chunk.task.context_id
                for artifact in chunk.task.artifacts:
                    for p in artifact.parts:
                        parts.extend(_extract_parts(p))
            elif chunk.HasField("message"):
                for p in chunk.message.parts:
                    parts.extend(_extract_parts(p))

    if not parts:
        parts = [{"kind": "text", "text": "(No textual response returned by agent.)"}]
    return JSONResponse({"parts": parts})


# Serve static web UI
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
