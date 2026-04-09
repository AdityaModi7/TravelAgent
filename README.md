# TravelAgent

An experimental travel-planning agent built to study how well an agent handles multi-turn conversations, memory updates, and long-horizon context degradation.

This project was created as part of research into:
- building agents for specific tasks
- testing multi-turn conversation behavior
- observing how memory degrades over time
- evaluating how well an agent replaces stale information instead of appending contradictory facts
- supporting a larger research argument about long-context reliability

## What it does

The project creates a travel planner agent with structured memory blocks for:
- traveler profile
- trip details
- bookings
- companions
- agent behavior rules

It then runs scripted conversation scenarios that stress-test the agent across short and long conversations, including:
- preferences and constraints
- changing plans
- contradictory updates
- buried details inside casual conversation
- multiple companions
- checkpoint questions that verify recall accuracy

## Main files

- [Create_Agent.py](Create_Agent.py): creates the travel agent and saves the agent ID to config
- [Run_Test.py](Run_Test.py): runs a selected scenario against the saved agent and records results
- [scenario.py](scenario.py): 50-turn scenario
- [scenario_100.py](scenario_100.py): 100-turn scenario
- [scenario_1000.py](scenario_1000.py): 1000-turn scenario assembled from parts
- [agent_config.json](agent_config.json): stores the created agent ID and model
- [results_*.json](.): saved evaluation outputs from prior runs

## Requirements

- Python 3.10+
- A Letta API key
- A `.env` file with `LETTA_API_KEY`

## Setup

1. Create and activate a virtual environment.
2. Install the project dependencies.
3. Add your API key to `.env`:

```bash
LETTA_API_KEY=your_key_here
```

## Usage

### Create the agent

Run the agent creation script once to generate a new agent and write its ID into `agent_config.json`.

### Run a test scenario

The test runner loads a scenario module and sends each user turn to the agent.

Examples:
- default 50-turn run: `python Run_Test.py`
- 100-turn run: `python Run_Test.py scenario_100`
- 1000-turn run: `python Run_Test.py scenario_1000`

Each run produces a timestamped results file containing:
- all turns
- tool calls
- checkpoint evaluations
- summary metrics
- timing data
- final memory state

## Research purpose

This is not a production travel assistant. It is a controlled experiment designed to expose failure modes in memory handling over time.

The main question is whether an agent can:
- retain correct facts
- update information cleanly when plans change
- ignore stale or contradicted details
- recover relevant context after many turns
- maintain useful behavior under long conversational load

## Notes

- Checkpoint turns are used to measure whether the agent still remembers key details.
- The scenarios intentionally include contradictions and late additions to test robustness.
- Older results files are preserved so runs can be compared over time.

## License

No license has been specified yet.
