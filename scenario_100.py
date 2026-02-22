"""
100-Turn Travel Planner Stress Test
====================================
Turns 1-50: Identical to the original 50-turn scenario.
Turns 51-100: Extended planning with more changes, new companions,
additional bookings, and increasing complexity to test memory degradation.

The scenario continues Sarah and Tom's Europe trip with more modifications,
a second trip discussion, and increasingly buried/conflicting information.
"""

SCENARIO = [
    # =========================================================================
    # PHASE 1: Basic information gathering (Turns 1-8) — same as 50-turn
    # =========================================================================
    {
        "turn": 1,
        "message": "Hi! I'm Sarah and I'm looking to plan a trip to Europe this summer.",
        "checkpoint": False,
        "notes": "Basic intro"
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
        "notes": "General question"
    },
    {
        "turn": 5,
        "message": "Rome sounds great! Let's add that. And maybe Barcelona too.",
        "checkpoint": False,
        "notes": "Itinerary: Paris, Rome, Barcelona"
    },
    {
        "turn": 6,
        "message": "Oh I should mention, I'm vegetarian. Pretty strict about it actually.",
        "checkpoint": False,
        "notes": "Dietary restriction"
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

    # =========================================================================
    # PHASE 2: Adding companion (Turns 9-15) — same as 50-turn
    # =========================================================================
    {
        "turn": 9,
        "message": "So my husband Tom is going to join me! He's super excited.",
        "checkpoint": False,
        "notes": "New companion"
    },
    {
        "turn": 10,
        "message": "Tom has a severe nut allergy, like epi-pen level serious. We always have to be careful at restaurants.",
        "checkpoint": False,
        "notes": "Critical health info"
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
        "notes": "Travel preference"
    },
    {
        "turn": 14,
        "message": "Oh and Tom's passport expires in September 2026, so we should be fine right?",
        "checkpoint": False,
        "notes": "Passport expiry"
    },
    {
        "turn": 15,
        "message": "What do you know about Tom so far?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Tom", "nut allergy", "museum", "passport"],
            "must_not_contain": [],
            "description": "Agent should recall all companion details"
        }
    },

    # =========================================================================
    # PHASE 3: Making bookings (Turns 16-22) — same as 50-turn
    # =========================================================================
    {
        "turn": 16,
        "message": "Let's start booking things. For Paris, I found the Hotel Le Petit Moulin. 4 nights, June 2-6, costs $180 per night.",
        "checkpoint": False,
        "notes": "First booking"
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
        "notes": "Flight bookings"
    },
    {
        "turn": 20,
        "message": "How much have we spent so far with all the bookings? Are we still within budget?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["8,000|8000"],
            "must_not_contain": [],
            "description": "Agent should calculate total and reference $8000 budget"
        }
    },
    {
        "turn": 21,
        "message": "Can you list all our bookings in order?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Le Petit Moulin", "Campo de' Fiori", "Casa Bonay", "Delta", "JFK"],
            "must_not_contain": [],
            "description": "Agent should recall all bookings"
        }
    },
    {
        "turn": 22,
        "message": "What are some good vegetarian restaurants near our Paris hotel?",
        "checkpoint": False,
        "notes": "Agent should remember vegetarian without being reminded"
    },

    # =========================================================================
    # PHASE 4: Changes and contradictions (Turns 23-32) — same as 50-turn
    # =========================================================================
    {
        "turn": 23,
        "message": "Bad news -- the Hotel Le Petit Moulin in Paris is fully booked. I need to switch to Hotel Monge instead. Same dates, June 2-6, but it's $200 per night.",
        "checkpoint": False,
        "notes": "CONTRADICTION: Paris hotel changes"
    },
    {
        "turn": 24,
        "message": "Actually you know what, let's skip Barcelona entirely. Tom just told me he'd rather spend more time in Rome.",
        "checkpoint": False,
        "notes": "MAJOR CHANGE: Remove Barcelona"
    },
    {
        "turn": 25,
        "message": "So let's extend Rome to June 6-14 instead. Can we keep the same hotel?",
        "checkpoint": False,
        "notes": "Update Rome dates"
    },
    {
        "turn": 26,
        "message": "We'll need to change the return flight too. Now it should be from Rome back to JFK on June 14 instead of Barcelona.",
        "checkpoint": False,
        "notes": "Update return flight"
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
            "description": "Agent should show ONLY current bookings. No old info."
        }
    },
    {
        "turn": 29,
        "message": "Oh also I forgot to mention -- I actually need to update my budget. My company is covering $2000 of the trip as a work perk, so our total budget is now $10,000.",
        "checkpoint": False,
        "notes": "Budget update: $8000 to $10000"
    },
    {
        "turn": 30,
        "message": "With the new budget and updated bookings, how much do we have left to spend on food, activities, and trains?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["10,000|10000"],
            "must_not_contain": ["8,000|8000"],
            "description": "Agent should use NEW budget of $10000"
        }
    },
    {
        "turn": 31,
        "message": "Tom just reminded me he's actually not just allergic to nuts -- he's allergic to all tree nuts AND peanuts. Can you make sure that's noted?",
        "checkpoint": False,
        "notes": "Update allergy info"
    },
    {
        "turn": 32,
        "message": "What dietary restrictions do we need to keep in mind for restaurants?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian", "tree nuts", "peanuts"],
            "must_not_contain": [],
            "description": "Agent should recall both dietary restrictions"
        }
    },

    # =========================================================================
    # PHASE 5: Buried info and companions (Turns 33-40) — same as 50-turn
    # =========================================================================
    {
        "turn": 33,
        "message": "I was reading about pickpockets in Rome and got a bit nervous. Anyway, Tom's phone number is +1-555-0147 in case the hotel needs an emergency contact. What areas should we avoid?",
        "checkpoint": False,
        "notes": "BURIED INFO: Phone number"
    },
    {
        "turn": 34,
        "message": "My sister might actually meet us in Rome for a couple days! Her name is Emily. She's 28 and she's flying in from London.",
        "checkpoint": False,
        "notes": "NEW COMPANION: Emily"
    },
    {
        "turn": 35,
        "message": "Emily is gluten-free by the way. Finding restaurants that work for all three of us might be tricky haha.",
        "checkpoint": False,
        "notes": "Emily dietary restriction"
    },
    {
        "turn": 36,
        "message": "What's the weather usually like in Rome in mid-June?",
        "checkpoint": False,
        "notes": "General question"
    },
    {
        "turn": 37,
        "message": "Oh I just realized -- Emily is actually arriving June 8, not when we get there. And she's leaving June 12.",
        "checkpoint": False,
        "notes": "Emily date update"
    },
    {
        "turn": 38,
        "message": "Can you tell me everything you know about everyone coming on this trip?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "vegetarian", "Tom", "nut", "peanut", "Emily", "gluten", "London"],
            "must_not_contain": [],
            "description": "Agent should know all three travelers"
        }
    },
    {
        "turn": 39,
        "message": "We should find a restaurant in Rome that works for a vegetarian, someone with tree nut and peanut allergies, and someone who's gluten-free. Any ideas?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian", "nut", "gluten"],
            "must_not_contain": [],
            "description": "CROSS-BLOCK SYNTHESIS: combine dietary info from multiple people"
        }
    },
    {
        "turn": 40,
        "message": "Actually, Emily just texted me -- she can't come anymore. Work emergency. So it's back to just me and Tom.",
        "checkpoint": False,
        "notes": "REMOVE COMPANION: Emily cancelled"
    },

    # =========================================================================
    # PHASE 6: Final stress original (Turns 41-50) — same as 50-turn
    # =========================================================================
    {
        "turn": 41,
        "message": "I've been thinking and I want to add a day trip from Rome to Florence on June 10. Not overnight, just a train there and back.",
        "checkpoint": False,
        "notes": "New activity"
    },
    {
        "turn": 42,
        "message": "For the Florence day trip, I want to visit the Uffizi Gallery. Tom will love it -- he's the museum guy remember?",
        "checkpoint": False,
        "notes": "References stored preference"
    },
    {
        "turn": 43,
        "message": "Our anniversary is June 5 actually! We'll be in Paris. Can you suggest something romantic for dinner that night? Remember my dietary needs.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian"],
            "must_not_contain": ["Barcelona", "Emily"],
            "description": "Agent should remember vegetarian and not mention cancelled plans"
        }
    },
    {
        "turn": 44,
        "message": "Oh and my email is sarah.martinez@gmail.com if you need it for any booking confirmations.",
        "checkpoint": False,
        "notes": "Email stored"
    },
    {
        "turn": 45,
        "message": "Wait I gave you Tom's phone number earlier right? What was it?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["555-0147"],
            "must_not_contain": [],
            "description": "Recall buried phone number from turn 33"
        }
    },
    {
        "turn": 46,
        "message": "And what's my email?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["sarah.martinez@gmail.com"],
            "must_not_contain": [],
            "description": "Recall email"
        }
    },
    {
        "turn": 47,
        "message": "Okay let's do a final review. Can you give me the complete trip plan from start to finish?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "Tom", "Paris", "Hotel Monge", "June 2", "Rome", "Campo de' Fiori", "June 14", "Florence", "Uffizi"],
            "must_not_contain": ["Barcelona", "Le Petit Moulin", "Casa Bonay", "Emily", "8000"],
            "description": "COMPREHENSIVE RECALL at turn 47"
        }
    },
    {
        "turn": 48,
        "message": "What's our total budget and how much have we spent on bookings?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["10,000|10000"],
            "must_not_contain": ["8,000|8000"],
            "description": "Budget should be $10000"
        }
    },
    {
        "turn": 49,
        "message": "List everyone who is coming on this trip and any dietary or health concerns for each person.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "vegetarian", "Tom", "tree nut", "peanut"],
            "must_not_contain": ["Emily", "gluten"],
            "description": "Only Sarah and Tom. Emily removed."
        }
    },
    {
        "turn": 50,
        "message": "Perfect, I think we're all set! Thanks for all your help planning this.",
        "checkpoint": False,
        "notes": "End of original 50-turn scenario"
    },

    # =========================================================================
    # PHASE 7: More bookings and activities (Turns 51-60)
    # =========================================================================
    {
        "turn": 51,
        "message": "Actually wait, I have a few more things. I want to book a cooking class in Rome. I found one called Roma Cooking Academy on June 8, costs $120 per person.",
        "checkpoint": False,
        "notes": "New activity booking with price"
    },
    {
        "turn": 52,
        "message": "And I want to do a Seine River cruise in Paris on June 3. It's $45 per person with Bateaux Mouches.",
        "checkpoint": False,
        "notes": "Another activity booking"
    },
    {
        "turn": 53,
        "message": "Tom also wants to do a Colosseum guided tour on June 7. I found one for $65 per person.",
        "checkpoint": False,
        "notes": "Third activity booking"
    },
    {
        "turn": 54,
        "message": "Oh and we need train tickets. Paris to Rome on June 6, I found tickets on Trenitalia for $85 per person.",
        "checkpoint": False,
        "notes": "Train booking"
    },
    {
        "turn": 55,
        "message": "Can you list all of our bookings and activities with their costs?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Hotel Monge", "Campo de' Fiori", "cooking", "Seine|cruise", "Colosseum", "Trenitalia|train"],
            "must_not_contain": ["Le Petit Moulin", "Casa Bonay", "Barcelona"],
            "description": "All current bookings and activities including new ones"
        }
    },
    {
        "turn": 56,
        "message": "How much have we spent total now including all the new activities and train tickets?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["10,000|10000"],
            "must_not_contain": ["8,000|8000"],
            "description": "Updated total spending against $10000 budget"
        }
    },
    {
        "turn": 57,
        "message": "What's a good area to walk around in Paris on our free afternoon on June 4?",
        "checkpoint": False,
        "notes": "General question"
    },
    {
        "turn": 58,
        "message": "Oh I forgot to mention, Tom is also lactose intolerant. Not as severe as the nut allergy but he avoids dairy when he can.",
        "checkpoint": False,
        "notes": "NEW dietary info added to existing companion"
    },
    {
        "turn": 59,
        "message": "What are all of Tom's dietary restrictions and health concerns now?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["tree nut|nut", "peanut", "lactose|dairy"],
            "must_not_contain": [],
            "description": "Agent should have ALL of Tom's restrictions including new lactose intolerance"
        }
    },
    {
        "turn": 60,
        "message": "Do you think the Roma Cooking Academy would be safe for Tom given his allergies?",
        "checkpoint": False,
        "notes": "Cross-referencing activity with companion health info"
    },

    # =========================================================================
    # PHASE 8: Second round of changes (Turns 61-70)
    # =========================================================================
    {
        "turn": 61,
        "message": "Bad news again. The Roma Cooking Academy just cancelled our class. Can you remove that booking?",
        "checkpoint": False,
        "notes": "Remove activity"
    },
    {
        "turn": 62,
        "message": "Instead let's do a food tour in Trastevere on June 8. It's called Eating Italy Food Tours, $89 per person.",
        "checkpoint": False,
        "notes": "Replace cancelled activity with new one"
    },
    {
        "turn": 63,
        "message": "Actually the Seine cruise I booked got moved to June 4 instead of June 3. Same price though.",
        "checkpoint": False,
        "notes": "Date change for existing activity"
    },
    {
        "turn": 64,
        "message": "My mom just called and she wants to join us in Paris! Her name is Linda, she's 58, and she's flying in from Chicago.",
        "checkpoint": False,
        "notes": "NEW COMPANION: Second companion added"
    },
    {
        "turn": 65,
        "message": "Mom has high blood pressure and takes medication for it. She also can't walk long distances so we need to keep that in mind.",
        "checkpoint": False,
        "notes": "Health concerns for new companion"
    },
    {
        "turn": 66,
        "message": "Linda is only joining us for Paris though, June 2-6. She's not coming to Rome.",
        "checkpoint": False,
        "notes": "Companion date constraint"
    },
    {
        "turn": 67,
        "message": "We'll need to upgrade the Paris hotel room since mom is joining. The upgraded room at Hotel Monge is $280 per night instead of $200.",
        "checkpoint": False,
        "notes": "Price update for existing booking"
    },
    {
        "turn": 68,
        "message": "Can you tell me about everyone on this trip and when they're with us?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "Tom", "Linda|mom", "Paris", "Rome"],
            "must_not_contain": ["Emily"],
            "description": "Three travelers with correct date ranges. No Emily."
        }
    },
    {
        "turn": 69,
        "message": "What are the health and dietary concerns for everyone traveling with us?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian", "nut|peanut", "lactose|dairy", "blood pressure"],
            "must_not_contain": ["gluten"],
            "description": "All health concerns for Sarah, Tom, and Linda. No gluten (Emily removed)."
        }
    },
    {
        "turn": 70,
        "message": "What does our Paris hotel booking look like now with the upgrade?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Hotel Monge", "280"],
            "must_not_contain": ["200"],
            "description": "Paris hotel should show $280/night, not old $200"
        }
    },

    # =========================================================================
    # PHASE 9: More changes and buried info (Turns 71-80)
    # =========================================================================
    {
        "turn": 71,
        "message": "I just realized our anniversary is June 5 and mom will be there. That's kind of awkward for a romantic dinner haha. Can we move the anniversary dinner to June 7 in Rome instead?",
        "checkpoint": False,
        "notes": "Move anniversary from Paris June 5 to Rome June 7"
    },
    {
        "turn": 72,
        "message": "Tell me about some nice places in Rome for an anniversary dinner. Remember all our dietary needs.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["vegetarian", "nut|peanut"],
            "must_not_contain": [],
            "description": "Anniversary dinner in Rome with dietary constraints"
        }
    },
    {
        "turn": 73,
        "message": "Linda's flight from Chicago arrives at CDG at 8am on June 2. Her confirmation code is LH4492. Oh and what time is our flight landing again?",
        "checkpoint": False,
        "notes": "BURIED: Linda's flight details in middle of question"
    },
    {
        "turn": 74,
        "message": "Tom just got a promotion at work by the way! He's now a senior architect at his firm. Anyway, do you think we should get travel insurance?",
        "checkpoint": False,
        "notes": "BURIED: Tom's job info in casual mention"
    },
    {
        "turn": 75,
        "message": "Actually our budget just went up again. Tom's promotion came with a bonus, so let's say $12,000 total now.",
        "checkpoint": False,
        "notes": "Third budget change: $8000 -> $10000 -> $12000"
    },
    {
        "turn": 76,
        "message": "What's our current budget?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["12,000|12000"],
            "must_not_contain": ["8,000|8000", "10,000|10000"],
            "description": "Budget should be $12000 only. Not $8000 or $10000."
        }
    },
    {
        "turn": 77,
        "message": "Oh no, mom just told me she needs to cancel. Work conflict came up. So it's back to just me and Tom again.",
        "checkpoint": False,
        "notes": "REMOVE COMPANION: Linda cancelled (second companion removal)"
    },
    {
        "turn": 78,
        "message": "Since mom isn't coming, let's downgrade the Paris hotel back to the original room. So Hotel Monge at $200 per night again.",
        "checkpoint": False,
        "notes": "Revert hotel price: $280 back to $200"
    },
    {
        "turn": 79,
        "message": "Who is currently coming on this trip?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "Tom"],
            "must_not_contain": ["Emily", "Linda|mom"],
            "description": "Only Sarah and Tom. Both Emily and Linda removed."
        }
    },
    {
        "turn": 80,
        "message": "What's the Paris hotel situation now?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Hotel Monge", "200"],
            "must_not_contain": ["280"],
            "description": "Hotel Monge back to $200/night after downgrade"
        }
    },

    # =========================================================================
    # PHASE 10: Final complexity and comprehensive recall (Turns 81-100)
    # =========================================================================
    {
        "turn": 81,
        "message": "I want to add another day trip. June 12, Rome to Pompeii. Tom will go crazy for the history there.",
        "checkpoint": False,
        "notes": "Second day trip"
    },
    {
        "turn": 82,
        "message": "For Pompeii I found a guided tour for $95 per person with Walks of Italy.",
        "checkpoint": False,
        "notes": "Activity booking for Pompeii"
    },
    {
        "turn": 83,
        "message": "Actually can we move the Colosseum tour from June 7 to June 9 instead? June 7 is our anniversary dinner now.",
        "checkpoint": False,
        "notes": "Reschedule activity to avoid anniversary conflict"
    },
    {
        "turn": 84,
        "message": "My address is 742 Evergreen Terrace, Springfield. Just in case the hotels need it for registration. What documents do we need for checking in?",
        "checkpoint": False,
        "notes": "BURIED: Home address in casual question"
    },
    {
        "turn": 85,
        "message": "List every activity and day trip we have planned with dates.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Seine|cruise", "Colosseum", "Florence|Uffizi", "food tour|Trastevere|Eating Italy", "Pompeii"],
            "must_not_contain": ["Roma Cooking Academy|cooking class"],
            "description": "All current activities. Cooking class was cancelled."
        }
    },
    {
        "turn": 86,
        "message": "Wait, what date is the Colosseum tour on now?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["June 9|9"],
            "must_not_contain": ["June 7"],
            "description": "Colosseum should be June 9, not June 7"
        }
    },
    {
        "turn": 87,
        "message": "Tom wants to know if there are any good jazz clubs in Rome. He's been getting into jazz lately. Oh and he also started learning Italian on Duolingo.",
        "checkpoint": False,
        "notes": "New interests for Tom buried in casual message"
    },
    {
        "turn": 88,
        "message": "I've been thinking about packing. What should I bring for two weeks in Europe in June?",
        "checkpoint": False,
        "notes": "General question"
    },
    {
        "turn": 89,
        "message": "Oh wait, the Eating Italy food tour in Trastevere just raised their price to $99 per person. Can you update that?",
        "checkpoint": False,
        "notes": "Price update for activity"
    },
    {
        "turn": 90,
        "message": "What's our total spending on everything now? Give me a complete breakdown.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Hotel Monge", "Campo de' Fiori", "12,000|12000"],
            "must_not_contain": ["8,000|8000", "Le Petit Moulin", "Casa Bonay", "Barcelona", "cooking academy|Roma Cooking"],
            "description": "Complete spending breakdown with $12000 budget. No cancelled items."
        }
    },
    {
        "turn": 91,
        "message": "What's my home address? I gave it to you earlier.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["742 Evergreen|Evergreen Terrace|Springfield"],
            "must_not_contain": [],
            "description": "Recall buried home address from turn 84"
        }
    },
    {
        "turn": 92,
        "message": "And what's Linda's flight confirmation code? I gave that to you too.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["LH4492"],
            "must_not_contain": [],
            "description": "Recall buried flight code from turn 73, even though Linda cancelled"
        }
    },
    {
        "turn": 93,
        "message": "What are all of Tom's interests and hobbies that you know about?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["museum|history", "jazz"],
            "must_not_contain": [],
            "description": "Should include both original interests and newly mentioned jazz"
        }
    },
    {
        "turn": 94,
        "message": "I want to change our return flight. I found a better deal -- United from Rome FCO to JFK on June 14, $550 per person instead of the Delta for $620.",
        "checkpoint": False,
        "notes": "Change airline AND price for return flight"
    },
    {
        "turn": 95,
        "message": "What airline is our return flight on now?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["United"],
            "must_not_contain": ["Delta"],
            "description": "Return flight should be United, not Delta"
        }
    },
    {
        "turn": 96,
        "message": "Actually, I also want to change the outbound flight. Found a direct American Airlines flight JFK to CDG on June 2 for $600 per person.",
        "checkpoint": False,
        "notes": "Change outbound flight too"
    },
    {
        "turn": 97,
        "message": "What are both of our flights now?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["American", "United"],
            "must_not_contain": ["Delta"],
            "description": "Both flights changed. No Delta anywhere."
        }
    },
    {
        "turn": 98,
        "message": "Give me the complete, final trip plan with every single detail. Every booking, every activity, every person, every dietary restriction, budget, everything.",
        "checkpoint": True,
        "expected": {
            "must_contain": ["Sarah", "vegetarian", "Tom", "nut|peanut", "lactose|dairy", "Hotel Monge", "200", "Campo de' Fiori", "150", "American", "United", "12,000|12000", "Florence", "Uffizi", "Pompeii", "Colosseum", "food tour|Trastevere|Eating Italy", "Seine|cruise", "anniversary"],
            "must_not_contain": ["Barcelona", "Le Petit Moulin", "Casa Bonay", "Emily", "gluten", "Linda", "Delta", "8,000|8000", "Roma Cooking Academy|cooking class", "280"],
            "description": "ULTIMATE COMPREHENSIVE RECALL: Everything correct, nothing outdated"
        }
    },
    {
        "turn": 99,
        "message": "How much budget do we have remaining after everything?",
        "checkpoint": True,
        "expected": {
            "must_contain": ["12,000|12000"],
            "must_not_contain": ["8,000|8000", "10,000|10000"],
            "description": "Final budget calculation from $12000"
        }
    },
    {
        "turn": 100,
        "message": "Amazing, thank you so much for all the help! This is going to be an incredible trip.",
        "checkpoint": False,
        "notes": "End of 100-turn scenario"
    }
]

# Print scenario summary
if __name__ == "__main__":
    total = len(SCENARIO)
    checkpoints = [s for s in SCENARIO if s["checkpoint"]]
    print(f"Travel Planner Stress Test Scenario (100-turn)")
    print(f"  Total turns: {total}")
    print(f"  Checkpoint turns: {len(checkpoints)}")
    print(f"  Regular turns: {total - len(checkpoints)}")
    print(f"\nCheckpoints:")
    for cp in checkpoints:
        print(f"  Turn {cp['turn']}: {cp['expected']['description']}")