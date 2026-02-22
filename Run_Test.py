"""
Travel Planner Stress Test Runner
==================================
Usage:
  python run_test.py                  # runs default scenario.py (50 turns)
  python run_test.py scenario_100     # runs scenario_100.py (100 turns)
  python run_test.py scenario_200     # runs scenario_200.py (200 turns)
"""

from letta_client import Letta
from dotenv import load_dotenv
import os
import sys
import json
import time
import importlib
from datetime import datetime

load_dotenv()

# Load scenario from command line argument or default
scenario_module = sys.argv[1] if len(sys.argv) > 1 else "scenario"
try:
    mod = importlib.import_module(scenario_module)
    SCENARIO = mod.SCENARIO
    print(f"Loaded scenario: {scenario_module} ({len(SCENARIO)} turns)")
except ImportError:
    print(f"ERROR: Could not find {scenario_module}.py")
    sys.exit(1)

client = Letta(api_key=os.getenv("LETTA_API_KEY"))

# Load agent config
with open("agent_config.json", "r") as f:
    config = json.load(f)

AGENT_ID = config["agent_id"]
print(f"Using agent: {config['agent_name']} ({AGENT_ID})")
print(f"Running {len(SCENARIO)} turn scenario...\n")

# Storage for results
results = {
    "agent_id": AGENT_ID,
    "model": config["model"],
    "scenario": scenario_module,
    "total_turns": len(SCENARIO),
    "start_time": datetime.now().isoformat(),
    "turns": [],
    "checkpoint_results": [],
    "summary": {}
}


def extract_tool_calls(messages):
    """Extract tool calls from agent response messages"""
    tool_calls = []
    for msg in messages:
        msg_type = getattr(msg, 'message_type', '')
        if msg_type == 'tool_call_message':
            tool_call = getattr(msg, 'tool_call', None)
            if tool_call:
                tool_calls.append({
                    "tool": getattr(tool_call, 'name', 'unknown'),
                    "arguments": getattr(tool_call, 'arguments', '{}')
                })
    return tool_calls


def extract_assistant_response(messages):
    """Extract the assistant's text response"""
    for msg in messages:
        if getattr(msg, 'message_type', '') == 'assistant_message':
            return getattr(msg, 'content', '')
    return ""


def evaluate_checkpoint(response_text, expected):
    """Evaluate a checkpoint response against expected criteria.
    Supports pipe-separated alternatives: 'term1|term2' matches if any variant found.
    """
    response_lower = response_text.lower()

    passed_contains = []
    failed_contains = []
    for term in expected["must_contain"]:
        alternatives = term.split("|")
        if any(alt.lower() in response_lower for alt in alternatives):
            passed_contains.append(term)
        else:
            failed_contains.append(term)

    passed_excludes = []
    failed_excludes = []
    for term in expected.get("must_not_contain", []):
        alternatives = term.split("|")
        if any(alt.lower() in response_lower for alt in alternatives):
            failed_excludes.append(term)
        else:
            passed_excludes.append(term)

    total_checks = len(expected["must_contain"]) + len(expected.get("must_not_contain", []))
    passed_checks = len(passed_contains) + len(passed_excludes)
    score = passed_checks / total_checks if total_checks > 0 else 1.0

    return {
        "score": score,
        "passed_contains": passed_contains,
        "failed_contains": failed_contains,
        "passed_excludes": passed_excludes,
        "failed_excludes": failed_excludes,
        "all_passed": len(failed_contains) == 0 and len(failed_excludes) == 0
    }


# Run the scenario
total_turns = len(SCENARIO)
print("=" * 70)
for step in SCENARIO:
    turn_num = step["turn"]
    message = step["message"]

    print(f"\n--- Turn {turn_num}/{total_turns} ---")
    print(f"User: {message[:80]}{'...' if len(message) > 80 else ''}")

    start_time = time.time()
    try:
        response = client.agents.messages.create(
            agent_id=AGENT_ID,
            messages=[{"role": "user", "content": message}]
        )
        elapsed = time.time() - start_time

        assistant_text = extract_assistant_response(response.messages)
        tool_calls = extract_tool_calls(response.messages)

        print(f"Agent: {assistant_text[:100]}{'...' if len(assistant_text) > 100 else ''}")
        if tool_calls:
            for tc in tool_calls:
                print(f"   Tool: {tc['tool']}({tc['arguments'][:60]}...)")
        print(f"   Time: {elapsed:.1f}s")

        turn_result = {
            "turn": turn_num,
            "user_message": message,
            "agent_response": assistant_text,
            "tool_calls": tool_calls,
            "elapsed_seconds": elapsed,
            "is_checkpoint": step["checkpoint"]
        }

        if step["checkpoint"]:
            eval_result = evaluate_checkpoint(assistant_text, step["expected"])
            turn_result["checkpoint_eval"] = eval_result

            status = "PASS" if eval_result["all_passed"] else "FAIL"
            print(f"\n   CHECKPOINT: {status} (score: {eval_result['score']:.2f})")
            print(f"   Description: {step['expected']['description']}")

            if eval_result["failed_contains"]:
                print(f"   Missing: {eval_result['failed_contains']}")
            if eval_result["failed_excludes"]:
                print(f"   Should NOT contain: {eval_result['failed_excludes']}")

            results["checkpoint_results"].append({
                "turn": turn_num,
                "description": step["expected"]["description"],
                "score": eval_result["score"],
                "passed": eval_result["all_passed"],
                "details": eval_result
            })

        results["turns"].append(turn_result)

    except Exception as e:
        print(f"   ERROR: {str(e)}")
        results["turns"].append({
            "turn": turn_num,
            "user_message": message,
            "error": str(e)
        })

    time.sleep(1)

# Final summary
print("\n" + "=" * 70)
print(f"\nEVALUATION SUMMARY ({scenario_module})")
print("=" * 70)

total_checkpoints = len(results["checkpoint_results"])
passed_checkpoints = sum(1 for cp in results["checkpoint_results"] if cp["passed"])
total_score = sum(cp["score"] for cp in results["checkpoint_results"]) / total_checkpoints if total_checkpoints > 0 else 0

results["summary"] = {
    "total_turns": len(SCENARIO),
    "total_checkpoints": total_checkpoints,
    "passed_checkpoints": passed_checkpoints,
    "failed_checkpoints": total_checkpoints - passed_checkpoints,
    "overall_score": total_score,
    "end_time": datetime.now().isoformat()
}

print(f"\nTotal checkpoints: {total_checkpoints}")
print(f"Passed: {passed_checkpoints}")
print(f"Failed: {total_checkpoints - passed_checkpoints}")
print(f"Overall score: {total_score:.2%}")

print(f"\nCheckpoint details:")
for cp in results["checkpoint_results"]:
    status = "PASS" if cp["passed"] else "FAIL"
    print(f"  [{status}] Turn {cp['turn']}: {cp['description']} (score: {cp['score']:.2f})")

# Save results
output_file = f"results_{scenario_module}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(output_file, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nFull results saved to {output_file}")

# Dump final memory state
print("\nFinal Memory Block State:")
print("=" * 70)
try:
    agent = client.agents.retrieve(agent_id=AGENT_ID)
    for block in agent.memory.blocks:
        print(f"\n[{block.label}]")
        print(f"{block.value}")
        print("-" * 40)
except Exception as e:
    print(f"Could not retrieve final memory state: {e}")