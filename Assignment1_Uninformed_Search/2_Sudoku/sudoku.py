import time
from collections import deque
from pathlib import Path

RESULT_FILE = Path(__file__).with_name("results.txt")

LEVELS = {
    "Easy":   "530070000600195000098000060800060003400803001700020006060000280000419005000080079",
    "Medium": "000260701680070090190004500820100040004602900050003028009300074040050036703018000",
    "Hard":   "000000907000420180000705026100904000050000040000507009920108000034059000507000000",
}


def is_allowed(board, i, v):
    r, c = i // 9, i % 9
    for k in range(9):
        if board[r * 9 + k] == v or board[k * 9 + c] == v:
            return False
    br, bc = r - r % 3, c - c % 3
    for x in range(3):
        for y in range(3):
            if board[(br + x) * 9 + bc + y] == v:
                return False
    return True


def duplicates(values):
    values = [v for v in values if v != 0]
    return len(values) - len(set(values))


def objective(board):
    f = board.count(0)
    for i in range(9):
        f += duplicates(board[i * 9:i * 9 + 9])
        f += duplicates(board[i::9])
    for br in (0, 3, 6):
        for bc in (0, 3, 6):
            box = []
            for x in range(3):
                box += board[(br + x) * 9 + bc:(br + x) * 9 + bc + 3]
            f += duplicates(box)
    return f


def bfs(sudoku):
    queue = deque([sudoku])
    nodes = 0
    max_queue = 1
    while queue:
        board = queue.popleft()
        nodes += 1
        if 0 not in board:
            return board, nodes, max_queue
        i = board.index(0)
        for v in range(1, 10):
            if is_allowed(board, i, v):
                new_board = board[:]
                new_board[i] = v
                queue.append(new_board)
        max_queue = max(max_queue, len(queue))
    return None, nodes, max_queue


def board_lines(board):
    lines = []
    for r in range(9):
        if r in (3, 6):
            lines.append("------+-------+------")
        row = board[r * 9:r * 9 + 9]
        lines.append("{} {} {} | {} {} {} | {} {} {}".format(*row))
    return lines


if __name__ == "__main__":
    lines = ["SUDOKU SOLVER - BFS with Backtracking"]
    for name, puzzle in LEVELS.items():
        start = [int(x) for x in puzzle]
        t0 = time.time()
        solution, nodes, max_queue = bfs(start)
        elapsed = time.time() - t0
        lines.append(f"\n===== {name} =====")
        lines.append(f"Empty cells: {start.count(0)}   f(start) = {objective(start)}")
        lines += board_lines(start)
        lines.append("\nSolution:")
        lines += board_lines(solution)
        lines.append(f"\nNodes expanded: {nodes}, max queue size: {max_queue}, "
                     f"time: {elapsed:.4f} s, f(solution) = {objective(solution)}")

    text = "\n".join(lines)
    print(text)
    RESULT_FILE.write_text(text + "\n", encoding="utf-8")
