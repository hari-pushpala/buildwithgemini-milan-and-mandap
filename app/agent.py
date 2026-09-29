# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.prompts import SYSTEM_INSTRUCTION
from app.tools import (
    evaluate_candidate_compatibility,
    search_wedding_venues_and_vendors,
    calculate_wedding_budget_plan,
    generate_wedding_itinerary,
)
from app.a2ui_utils import a2ui_callback

MODEL = "gemini-2.5-flash"

root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        evaluate_candidate_compatibility,
        search_wedding_venues_and_vendors,
        calculate_wedding_budget_plan,
        generate_wedding_itinerary,
    ],
    after_model_callback=a2ui_callback,
)

app = App(
    root_agent=root_agent,
    name="milan_and_mandap_app",
)
