# 2. Sudoku Solver – BFS with Backtracking

## 1. Problem model
A partially filled 9×9 grid is given. Every empty cell must be filled with a number from 1 to 9 so that
every row, every column and every 3×3 box contains each number exactly once.
The problem is modelled as a **CSP**. The program solves three levels: **Easy, Medium, Hard**.

## 2. Problem representation

| Element | Description |
|---|---|
| **Variables** | The empty cells `X(r, c)`, r, c ∈ {0..8} |
| **Domain** | D = {1, …, 9}; in practice only the values not already in the cell's row, column and box |
| **Constraints** | `alldifferent` for 9 rows, 9 columns and 9 boxes (27 constraints) |
| **State** | A list of 81 numbers (0 = empty cell) |
| **Initial state** | The given Sudoku |
| **Action** | Place an allowed value in the first empty cell |
| **Goal test** | No empty cells remain (since only allowed values are placed, f = 0 as well) |

## 3. Objective function

  f(board) = (number of empty cells) + Σ₍unit₎ (number of repeated values in the unit)

where a unit is a row, a column or a 3×3 box. f = 0 ⇔ the Sudoku is solved correctly.

## 4. Landscape (search space)

| | Size |
|---|---|
| Empty grid, naive: 9⁸¹ | ≈ 2 × 10⁷⁷ |
| Every row a permutation: (9!)⁹ | ≈ 1.1 × 10⁵⁰ |
| Valid Sudoku grids | ≈ 6.67 × 10²¹ |

| Level | Empty cells (k) | Naive landscape 9ᵏ |
|---|---|---|
| Easy | 51 | ≈ 4.6 × 10⁴⁸ |
| Medium | 45 | ≈ 8.7 × 10⁴² |
| Hard | 53 | ≈ 3.8 × 10⁵⁰ |

The branching factor is ≤ 9 and the depth of the tree is k (the number of empty cells).

## 5. Implementation – BFS with Backtracking (`sudoku.py`)

1. The initial state is placed in a **FIFO queue** (`deque`), which makes the search **Breadth First**.
2. The first state is taken from the queue; if it has no empty cells, the solution has been found.
3. Otherwise the first empty cell is located and the constraints are checked for each value from 1 to 9.
4. **Pruning instead of undoing:** only allowed values create new states; a branch where no value is allowed
   simply "dies" and the search continues with the other alternatives in the queue. Unlike DFS, no step is undone here,
   because each state is a separate copy; this is the role of backtracking in BFS.
5. The number of nodes, the maximum queue size and the time are measured.
6. The result is printed to the terminal and automatically saved to `results.txt`.

## 6. Results

| Level | Empty cells | Nodes expanded | Max queue | Time | f |
|---|---|---|---|---|---|
| Easy | 51 | 4,632 | 738 | < 0.1 s | 0 |
| Medium | 45 | 69 | 5 | < 0.01 s | 0 |
| Hard | 53 | 22,919 | 3,616 | < 0.6 s | 0 |

The initial boards and the solutions are in `results.txt`.

**Discussion:** BFS keeps an entire level of the tree in memory, so on Hard the queue reaches 3,616 states.
The difficulty for a human does not always match the number of BFS nodes (for example, Medium branches less than
Easy because its first empty cells have few candidates). For Sudoku, DFS would be more memory-efficient.
