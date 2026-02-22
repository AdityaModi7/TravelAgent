"""
Travel Planner Agent — GPT-4.1-nano 1000-turn test
"""
from letta_client import Letta
from dotenv import load_dotenv
import os
import json

load_dotenv()

MODEL = "openai/gpt-4o-mini"

client = Letta(api_key=os.getenv("LETTA_API_KEY"))

agent_state = client.agents.create(
    model=MODEL,
    memory_blocks=[
        {
            "label": "traveler_profile",
            "value": (
                "Traveler profile (update as user shares info):\n"
                "- Name: unknown\n"
                "- Dietary restrictions: unknown\n"
                "- Accommodation preference: unknown\n"
                "- Budget: unknown\n"
                "- Email: unknown\n"
            )
        },
        {
            "label": "trip_details",
            "value": (
                "Trip details (update as plans develop):\n"
                "- Destination(s): unknown\n"
                "- Dates: unknown\n"
                "- Duration: unknown\n"
                "- Transportation preference: unknown\n"
            )
        },
        {
            "label": "bookings",
            "value": (
                "Confirmed bookings (update when bookings change):\n"
                "- Hotels: none\n"
                "- Flights: none\n"
                "- Activities: none\n"
            )
        },
        {
            "label": "companions",
            "value": (
                "Travel companions (update as people are added/removed):\n"
                "- Currently: traveling solo\n"
            )
        },
        {
            "label": "persona",
            "value": (
                "You are a personal travel planning assistant. Rules:\n"
                "1) Always store important trip information in your memory when the user shares it.\n"
                "2) When information changes, use memory_replace to UPDATE the old info, don't just append.\n"
                "3) Keep memory blocks organized and accurate at all times.\n"
                "4) When making recommendations, always check your memory first for preferences and constraints.\n"
                "5) Pay attention to casual mentions -- users often drop important details mid-sentence.\n"
                "6) Track dietary restrictions, allergies, and health concerns carefully for ALL travelers.\n"
                "7) When a companion is removed from the trip, update the companions block accordingly.\n"
                "8) When bookings change, remove the old booking and add the new one.\n"
            )
        }
    ]
)

print("Agent created successfully!")
print(f"  Agent ID: {agent_state.id}")
print(f"  Model: {MODEL}")
print("")
print("Memory blocks:")
for block in agent_state.memory.blocks:
    print(f"  [{block.label}]")
    print(f"  {block.value[:80]}...")
    print()

with open("agent_config.json", "w") as f:
    json.dump({
        "agent_id": agent_state.id,
        "agent_name": "travel_planner_nano_1000",
        "model": MODEL
    }, f, indent=2)

print("Agent ID saved to agent_config.json")