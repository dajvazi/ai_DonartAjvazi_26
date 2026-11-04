import sys
import time
from pathlib import Path

RESULT_FILE = Path(__file__).with_name("results.txt")

nodes = 0


def is_allowed(m, r, c, v):
    if v in m[r]:
        return False
    for row in m:
        if row[c] == v:
            return False
    return True


def duplicates(values):
    values = [v for v in values if v != 0]
    return len(values) - len(set(values))


def objective(m):
    f = sum(row.count(0) for row in m)
    for i in range(len(m)):
        f += duplicates(m[i])
        f += duplicates([row[i] for row in m])
    return f


def dls(m, cell, limit):
    global nodes
    nodes += 1
    n = len(m)
    if cell == n * n:
        return True
    if cell == limit:
        return False
    r, c = cell // n, cell % n
    for v in range(1, n + 1):
        if is_allowed(m, r, c, v):
            m[r][c] = v
            if dls(m, cell + 1, limit):
                return True
            m[r][c] = 0
    return False


def iddfs(n):
    for limit in range(n * n + 1):
        m = [[0] * n for _ in range(n)]
        if dls(m, 0, limit):
            return m, limit
    return None, None


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("n = "))
    if n < 1:
        sys.exit("n must be at least 1")
    t0 = time.time()
    m, limit = iddfs(n)
    elapsed = time.time() - t0

    lines = ["LATIN SQUARE - IDDFS with Backtracking", f"Input: {n}", "Output:"]
    for row in m:
        lines.append(" ".join(map(str, row)))
    lines.append(f"\nDepth where the solution was found: {limit}")
    lines.append(f"Total nodes (all iterations): {nodes}")
    lines.append(f"Time: {elapsed:.2f} s")
    lines.append(f"Objective function f = {objective(m)}")

    text = "\n".join(lines)
    print(text)
    RESULT_FILE.write_text(text + "\n", encoding="utf-8")
