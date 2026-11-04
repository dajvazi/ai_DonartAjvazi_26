import time
from itertools import combinations
from pathlib import Path

RESULT_FILE = Path(__file__).with_name("results.txt")

PLAYERS = 32
GROUPS = 8
GROUP_SIZE = 4
WEEKS = 9

nodes = 0


def find_keys():
    keys = set()
    for a in range(1, PLAYERS):
        for b in range(a + 1, PLAYERS):
            keys.add(tuple(sorted((a, b, a ^ b))))
    return sorted(keys)


def week_groups(key):
    a, b, c = key
    groups = []
    for x in range(PLAYERS):
        group = sorted([x, x ^ a, x ^ b, x ^ c])
        if group not in groups:
            groups.append(group)
    return groups


def objective(schedule):
    meetings = {}
    for week in schedule:
        for group in week:
            for pair in combinations(group, 2):
                meetings[pair] = meetings.get(pair, 0) + 1
    return sum(v - 1 for v in meetings.values() if v > 1)


def valid_partition(schedule):
    for week in schedule:
        players = sorted(x for group in week for x in group)
        if len(week) != GROUPS or players != list(range(PLAYERS)):
            return False
        if any(len(group) != GROUP_SIZE for group in week):
            return False
    return True


def has_conflict(key, chosen):
    for other in chosen:
        if set(key) & set(other):
            return True
    return False


def dfs(keys, chosen, start):
    global nodes
    nodes += 1
    if len(chosen) == WEEKS:
        return True
    for i in range(start, len(keys)):
        if has_conflict(keys[i], chosen):
            continue
        chosen.append(keys[i])
        if dfs(keys, chosen, i + 1):
            return True
        chosen.pop()
    return False


if __name__ == "__main__":
    t0 = time.time()
    chosen = []
    dfs(find_keys(), chosen, 0)
    elapsed = time.time() - t0
    schedule = [week_groups(key) for key in chosen]

    lines = [
        "SOCIAL GOLFERS PROBLEM - DFS with Backtracking",
        f"Players: {PLAYERS}, groups: {GROUPS}, players per group: {GROUP_SIZE}",
        f"Theoretical bound: {(PLAYERS - 1) // (GROUP_SIZE - 1)} weeks",
        f"Weeks found: {len(schedule)}",
        f"Nodes visited: {nodes}",
        f"Time: {elapsed:.4f} s",
        f"Valid partition every week: {valid_partition(schedule)}",
        f"Objective function f = {objective(schedule)}\n",
        "        " + "".join(f"Group {g + 1:<7}" for g in range(GROUPS)),
    ]
    for i, week in enumerate(schedule, 1):
        line = f"Week {i:<2} "
        for group in week:
            line += f"{','.join(map(str, group)):<13}"
        lines.append(line)

    text = "\n".join(lines)
    print(text)
    RESULT_FILE.write_text(text + "\n", encoding="utf-8")
