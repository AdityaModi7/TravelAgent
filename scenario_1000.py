"""
1000-Turn Travel Planner Stress Test
Combines: scenario_100 (1-100) + part1 (101-400) + middle (401-765) + final (766-1000)
"""
from scenario_1000_part1 import SCENARIO as PART1
from scenario_1000_middle import SCENARIO_MIDDLE
from scenario_1000_final import SCENARIO_FINAL

SCENARIO = list(PART1) + SCENARIO_MIDDLE + SCENARIO_FINAL

if __name__ == "__main__":
    total = len(SCENARIO)
    checkpoints = [s for s in SCENARIO if s["checkpoint"]]
    turns = [s["turn"] for s in SCENARIO]
    from collections import Counter
    dupes = [t for t, c in Counter(turns).items() if c > 1]
    gaps = [(turns[i], turns[i+1]) for i in range(len(turns)-1) if turns[i+1] != turns[i]+1]
    print(f"Total turns: {total}")
    print(f"Checkpoints: {len(checkpoints)}")
    print(f"First: {turns[0]}, Last: {turns[-1]}")
    print(f"Duplicates: {dupes[:5] if dupes else 'None'}")
    print(f"Gaps: {gaps[:5] if gaps else 'None'}")