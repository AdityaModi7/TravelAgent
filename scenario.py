"""
50-Turn Travel Planner Stress Test
==================================
A scripted multi-turn conversation that simulates a realistic trip planning session.
Designed to test memory storage, updates, contradictions, cross-block reasoning,
and implicit information handling.

Checkpoint turns are marked with [CHECKPOINT] and include expected answers.
Regular turns just send messages and let the agent respond naturally.

The scenario follows Sarah planning a 2-week Europe trip with her husband Tom.
"""

SCENARIO = [
    # === PHASE 1: Basic information gathering (Turns 1-8) ===
    {
        "turn": 1,
        "message": "Hi! I'm Sarah and I'm looking to plan a trip to Europe this summer.",
        "checkpoint": False,
        "notes": "Basic intro — agent should store name and trip interest"
    },
    {
        "turn": 2,
        "message": "I'm thinking sometime in June, maybe 2 weeks? My budget is around $8,000 total.",
        "checkpoint": False,
        "notes": "Key facts: June, 2 weeks, $8000 budget"
    },
    {
        "turn": 3,
        "message": "I definitely want to visit Paris. I've always dreamed of seeing the Eiffel Tower.",
        "checkpoint": False,
        "notes": "First city preference"
    },
    {
        "turn": 4,
        "message": "What other cities would you recommend that pair well with Paris?",
        "checkpoint": False,
        "notes": "General question — no memory update needed"
    },
    {
        "turn": 5,
        "message": "Rome sounds great! Let's add that. And maybe Barcelona too.",
        "checkpoint": False,
        "notes": "Itinerary: Paris → Rome → Barcelona"
    },
    {
        "turn": 6,
        "message": "Oh I should mention, I'm vegetarian. Pretty strict about it actually.",
        "checkpoint": False,
        "notes": "Dietary restriction — should be stored in traveler_profile"
    },
    {
        "turn": 7,
        "message": "I prefer boutique hotels over big chains. Nothing too fancy but clean and central.",
        "checkpoint": False,
        "notes": "Accommodation preference"
    },
    {
        "turn": 8,
        "message": "Can you summarize what we have so far for my trip?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "June", "8,000|8000", "Paris", "Rome", "Barcelona", "vegetarian", "boutique"],
            "must_not_contain": [],
            "description": "Agent should recall all basic trip details"
        }
    },

    # === PHASE 2: Adding a companion with constraints (Turns 9-15) ===
    {
        "turn": 9,
        "message": "So my husband Tom is going to join me! He's super excited.",
        "checkpoint": False,
        "notes": "New companion — should update companions block"
    },
    {
        "turn": 10,
        "message": "Tom has a severe nut allergy, like epi-pen level serious. We always have to be careful at restaurants.",
        "checkpoint": False,
        "notes": "Critical health info for companion"
    },
    {
        "turn": 11,
        "message": "He's also really into history and museums. He could spend all day in a museum honestly.",
        "checkpoint": False,
        "notes": "Companion preference"
    },
    {
        "turn": 12,
        "message": "What's the best way to get between the three cities?",
        "checkpoint": False,
        "notes": "General question"
    },
    {
        "turn": 13,
        "message": "Tom doesn't love flying short distances. Can we do trains between cities?",
        "checkpoint": False,
        "notes": "Travel preference — should be stored"
    },
    {
        "turn": 14,
        "message": "Oh and Tom's passport expires in September 2026, so we should be fine right?",
        "checkpoint": False,
        "notes": "Specific detail — passport expiry"
    },
    {
        "turn": 15,
        "message": "What do you know about Tom so far?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Tom", "nut allergy", "museum", "train", "passport"],
            "must_not_contain": [],
            "description": "Agent should recall all companion details including allergy, preferences, and passport"
        }
    },

    # === PHASE 3: Making specific bookings (Turns 16-22) ===
    {
        "turn": 16,
        "message": "Let's start booking things. For Paris, I found the Hotel Le Petit Moulin. 4 nights, June 2-6, costs $180 per night.",
        "checkpoint": False,
        "notes": "First booking — specific hotel with dates and price"
    },
    {
        "turn": 17,
        "message": "For Rome I'm looking at Hotel Campo de' Fiori. June 6-10, $150 per night.",
        "checkpoint": False,
        "notes": "Second booking"
    },
    {
        "turn": 18,
        "message": "And Barcelona, let's do Hotel Casa Bonay. June 10-14, $160 per night.",
        "checkpoint": False,
        "notes": "Third booking"
    },
    {
        "turn": 19,
        "message": "I found flights too. Delta from JFK to Paris CDG on June 2, $650 per person. And Barcelona to JFK on June 14, $580 per person.",
        "checkpoint": False,
        "notes": "Flight bookings with prices — two people so need to calculate"
    },
    {
        "turn": 20,
        "message": "How much have we spent so far with all the bookings? Are we still within budget?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["8,000|8000"],
            "must_not_contain": [],
            "description": "Agent should calculate: Hotels = (720+600+640) + Flights = (1300+1160) = $4420. Should note remaining budget from $8000."
        }
    },
    {
        "turn": 21,
        "message": "Can you list all our bookings in order?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Le Petit Moulin", "Campo de' Fiori", "Casa Bonay", "Delta", "JFK"],
            "must_not_contain": [],
            "description": "Agent should recall all bookings with correct details"
        }
    },
    {
        "turn": 22,
        "message": "What are some good vegetarian restaurants near our Paris hotel?",
        "checkpoint": False,
        "notes": "Agent should remember Sarah is vegetarian without being reminded"
    },

    # === PHASE 4: Changes and contradictions (Turns 23-32) ===
    {
        "turn": 23,
        "message": "Bad news — the Hotel Le Petit Moulin in Paris is fully booked. I need to switch to Hotel Monge instead. Same dates, June 2-6, but it's $200 per night.",
        "checkpoint": False,
        "notes": "CONTRADICTION: Paris hotel changes. Agent must replace, not append."
    },
    {
        "turn": 24,
        "message": "Actually you know what, let's skip Barcelona entirely. Tom just told me he'd rather spend more time in Rome.",
        "checkpoint": False,
        "notes": "MAJOR CHANGE: Remove Barcelona from itinerary AND cancel Barcelona hotel AND update trip timeline"
    },
    {
        "turn": 25,
        "message": "So let's extend Rome to June 6-14 instead. Can we keep the same hotel?",
        "checkpoint": False,
        "notes": "Update Rome dates from June 6-10 to June 6-14"
    },
    {
        "turn": 26,
        "message": "We'll need to change the return flight too. Now it should be from Rome back to JFK on June 14 instead of Barcelona.",
        "checkpoint": False,
        "notes": "Update return flight departure city"
    },
    {
        "turn": 27,
        "message": "I found a Rome to JFK flight on June 14 for $620 per person.",
        "checkpoint": False,
        "notes": "New return flight price"
    },
    {
        "turn": 28,
        "message": "Give me the updated full itinerary with all current bookings.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Hotel Monge", "Campo de' Fiori", "June 2-6", "June 6-14", "Rome", "Paris"],
            "must_not_contain": ["Le Petit Moulin", "Casa Bonay", "Barcelona"],
            "description": "Agent should show ONLY current bookings. No Barcelona, no old Paris hotel."
        }
    },
    {
        "turn": 29,
        "message": "Oh also I forgot to mention — I actually need to update my budget. My company is covering $2000 of the trip as a work perk, so our total budget is now $10,000.",
        "checkpoint": False,
        "notes": "Budget update: $8000 → $10000"
    },
    {
        "turn": 30,
        "message": "With the new budget and updated bookings, how much do we have left to spend on food, activities, and trains?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["10,000|10000"],
            "must_not_contain": ["8,000|8000"],
            "description": "Agent should use NEW budget of $10000, not old $8000. Calculate remaining after updated bookings."
        }
    },
    {
        "turn": 31,
        "message": "Tom just reminded me he's actually not just allergic to nuts — he's allergic to all tree nuts AND peanuts. Can you make sure that's noted?",
        "checkpoint": False,
        "notes": "Update/refine existing allergy info"
    },
    {
        "turn": 32,
        "message": "What dietary restrictions do we need to keep in mind for restaurants?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian", "tree nuts", "peanuts"],
            "must_not_contain": [],
            "description": "Agent should recall BOTH Sarah's vegetarian diet AND Tom's updated allergy details"
        }
    },

    # === PHASE 5: Buried information and casual mentions (Turns 33-40) ===
    {
        "turn": 33,
        "message": "I was reading about pickpockets in Rome and got a bit nervous. Anyway, Tom's phone number is +1-555-0147 in case the hotel needs an emergency contact. What areas should we avoid?",
        "checkpoint": False,
        "notes": "BURIED INFO: Phone number hidden in middle of unrelated question"
    },
    {
        "turn": 34,
        "message": "My sister might actually meet us in Rome for a couple days! Her name is Emily. She's 28 and she's flying in from London.",
        "checkpoint": False,
        "notes": "NEW COMPANION: Third person added late in planning"
    },
    {
        "turn": 35,
        "message": "Emily is gluten-free by the way. Finding restaurants that work for all three of us might be tricky haha.",
        "checkpoint": False,
        "notes": "Another dietary restriction for new companion"
    },
    {
        "turn": 36,
        "message": "What's the weather usually like in Rome in mid-June?",
        "checkpoint": False,
        "notes": "General question — no memory update"
    },
    {
        "turn": 37,
        "message": "Oh I just realized — Emily is actually arriving June 8, not when we get there. And she's leaving June 12.",
        "checkpoint": False,
        "notes": "Specific dates for companion overlap"
    },
    {
        "turn": 38,
        "message": "Can you tell me everything you know about everyone coming on this trip?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "vegetarian", "Tom", "nut", "peanut", "Emily", "gluten", "London"],
            "must_not_contain": [],
            "description": "Agent should know all three travelers and their dietary needs"
        }
    },
    {
        "turn": 39,
        "message": "We should find a restaurant in Rome that works for a vegetarian, someone with tree nut and peanut allergies, and someone who's gluten-free. Any ideas?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian", "nut", "gluten"],
            "must_not_contain": [],
            "description": "CROSS-BLOCK SYNTHESIS: Agent must combine dietary info from multiple people stored across blocks"
        }
    },
    {
        "turn": 40,
        "message": "Actually, Emily just texted me — she can't come anymore. Work emergency. So it's back to just me and Tom.",
        "checkpoint": False,
        "notes": "REMOVE COMPANION: Emily is cancelled. Agent should update companions block."
    },

    # === PHASE 6: Final stress and comprehensive recall (Turns 41-50) ===
    {
        "turn": 41,
        "message": "I've been thinking and I want to add a day trip from Rome to Florence on June 10. Not overnight, just a train there and back.",
        "checkpoint": False,
        "notes": "New activity within existing trip"
    },
    {
        "turn": 42,
        "message": "For the Florence day trip, I want to visit the Uffizi Gallery. Tom will love it — he's the museum guy remember?",
        "checkpoint": False,
        "notes": "References stored companion preference"
    },
    {
        "turn": 43,
        "message": "Our anniversary is June 5 actually! We'll be in Paris. Can you suggest something romantic for dinner that night? Remember my dietary needs.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian"],
            "must_not_contain": ["Barcelona", "Emily"],
            "description": "Agent should remember vegetarian restriction and that they're in Paris June 2-6. Should not mention cancelled plans."
        }
    },
    {
        "turn": 44,
        "message": "Oh and my email is sarah.martinez@gmail.com if you need it for any booking confirmations.",
        "checkpoint": False,
        "notes": "Arbitrary identifier — similar to the phone number test"
    },
    {
        "turn": 45,
        "message": "Wait I gave you Tom's phone number earlier right? What was it?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["555-0147"],
            "must_not_contain": [],
            "description": "Recall of buried phone number from turn 33"
        }
    },
    {
        "turn": 46,
        "message": "And what's my email?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["sarah.martinez@gmail.com"],
            "must_not_contain": [],
            "description": "Recall of recently shared email"
        }
    },
    {
        "turn": 47,
        "message": "Okay let's do a final review. Can you give me the complete trip plan from start to finish?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "Tom", "Paris", "Hotel Monge", "June 2", "Rome", "Campo de' Fiori", "June 14", "Florence", "Uffizi"],
            "must_not_contain": ["Barcelona", "Le Petit Moulin", "Casa Bonay", "Emily", "8000"],
            "description": "COMPREHENSIVE RECALL: Full trip with all updates applied. No cancelled items."
        }
    },
    {
        "turn": 48,
        "message": "What's our total budget and how much have we spent on bookings?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["10,000|10000"],
            "must_not_contain": ["8,000|8000"],
            "description": "Budget should be $10000. Bookings: Hotel Monge 4x200=800, Campo de Fiori 8x150=1200, flights 650x2+620x2=2540. Total ~$4540."
        }
    },
    {
        "turn": 49,
        "message": "List everyone who is coming on this trip and any dietary or health concerns for each person.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "vegetarian", "Tom", "tree nut", "peanut"],
            "must_not_contain": ["Emily", "gluten"],
            "description": "Only Sarah and Tom. Emily was removed. Her gluten-free restriction should NOT appear."
        }
    },
    {
        "turn": 50,
        "message": "Perfect, I think we're all set! Thanks for all your help planning this.",
        "checkpoint": False,
        "notes": "Closing message"
    }
]

# Print scenario summary
if __name__ == "__main__":
    total = len(SCENARIO)
    checkpoints = [s for s in SCENARIO if s["checkpoint"]]
    print(f"📋 Travel Planner Stress Test Scenario")
    print(f"   Total turns: {total}")
    print(f"   Checkpoint turns: {len(checkpoints)}")
    print(f"   Regular turns: {total - len(checkpoints)}")
    print(f"\n📍 Checkpoints:")
    for cp in checkpoints:
        print(f"   Turn {cp['turn']}: {cp['expected']['description']}")