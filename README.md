# 💍 Milan & Mandap: Agentic Matrimony & One-Stop Wedding Operating System

Built by [Hari Pushpala](https://github.com/hari-pushpala) for the **Build with Gemini World Tour**.

Powered by the **Google Agent Development Kit (ADK)**, **Gemini 2.5 Flash**, **A2A Protocol**, and deployed to **Google Cloud Vertex AI Agent Platform** & **Cloud Run**.

---

## 🌟 Overview & Problem Solved

Traditional matrimony apps act like noisy, filter-heavy digital phonebooks that lead to fatigue, catfishing, and family ideological conflict. Crucially, the incumbent relationship terminates the moment two candidates match—abandoning them at their most expensive, chaotic, and stressful phase: **Wedding Planning**.

**Milan & Mandap** is a unified, end-to-end autonomous platform:
1. **Agentic Compatibility & Multi-Factor Verification:** Autonomous candidate agents simulate deep values alignment across 20+ dimensions, conduct double-blind dealbreaker audits (finances, lifestyle, parenting), and verify real-world trust credentials (KYC, workplace verification, credit tiers).
2. **One-Stop Wedding Operating System:** Seamlessly transitions engaged couples into an intelligent wedding director that manages budget allocations, contractual milestone escrow releases (preventing vendor flaking), and day-of run-of-show itineraries.
3. **Rich UI Rendering (A2UI 0.8):** Emits structured cards natively within the chat stream.

---

## 🏗️ Architecture & Features

```
User (Browser) ──▶ FastAPI Proxy (Cloud Run) ──▶ Deployed Agent (Vertex AI Agent Runtime)
                                                      │
                       ┌──────────────────────────────┴──────────────────────────────┐
                       ▼                                                             ▼
           Matchmaking & Trust Engine                                    Wedding Operating System
  • evaluate_candidate_compatibility                             • search_wedding_venues_and_vendors
    (Agent-to-agent values audit, dealbreakers)                    (Escrow milestone protected venues/vendors)
  • Verified Credentials & Trust Scores                         • calculate_wedding_budget_plan
    (KYC, Workplace, AI Liveness)                                  (Dynamic budget split & emergency reserves)
                                                                 • generate_wedding_itinerary
                                                                   (Multi-day run-of-show & guest concierge)
```

---

## 🚀 Getting Started Locally

### 1. Prerequisites
- Python 3.11+
- Google Cloud Project with Vertex AI enabled (`GOOGLE_GENAI_USE_VERTEXAI=true`)

### 2. Run Unit Tests
```bash
python3 -m unittest discover tests
```

### 3. Run the Agent Locally via ADK Web
```bash
adk web app
```

### 4. Run the Branded Chat Web Frontend
```bash
cd frontend
python3 main.py
# Open http://localhost:8080 in your browser
```

---

## ☁️ Deployment

- **Agent Backend:** Deployed to **Vertex AI Agent Platform / Agent Runtime** via `agents-cli deploy`.
- **Frontend Proxy & A2UI Renderer:** Deployed to **Google Cloud Run**.

---

## 👤 Author
- **GitHub:** [@hari-pushpala](https://github.com/hari-pushpala)
