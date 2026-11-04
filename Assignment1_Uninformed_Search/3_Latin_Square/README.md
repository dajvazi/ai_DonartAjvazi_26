# 3. Latin Square – IDDFS with Backtracking

## 1. Problem model
A Latin square is an n×n grid filled with n different numbers (1..n), each appearing
exactly once in every row and every column. For the input n, the program prints an n×n Latin square.
The problem is modelled as a **CSP**.

Example (input 5): the example in the assignment shows 4 rows; the correct output has 5 rows.

## 2. Problem representation

| Element | Description |
|---|---|
| **Variables** | The cells `M[r][c]`, r, c ∈ {0..n−1} (n² variables) |
| **Domain** | D = {1, …, n} |
| **Constraints** | `alldifferent` for every row and every column (2n constraints) |
| **State** | The partial matrix (0 = empty cell) |
| **Initial state** | The empty matrix |
| **Action** | Place an allowed value in the next cell (row by row) |
| **Depth** | The number of filled cells; the solution is at depth n² |
| **Goal test** | All cells are filled (since only allowed values are placed, f = 0 as well) |

## 3. Objective function

  f(M) = (empty cells) + Σ₍rows₎ (repetitions) + Σ₍columns₎ (repetitions)

f = 0 ⇔ M is a Latin square.

## 4. Landscape (search space)

| | Formula | n = 5 |
|---|---|---|
| Naive assignments | n^(n²) | 5²⁵ ≈ 3 × 10¹⁷ |
| Every row a permutation | (n!)ⁿ | 120⁵ ≈ 2.5 × 10¹⁰ |
| Valid Latin squares | – | 161,280 |

Branching factor ≤ n, maximum depth n².

## 5. Implementation – IDDFS with Backtracking (`latin.py`)

1. **IDDFS** calls **Depth-Limited Search** with limit = 0, 1, 2, …, n².
2. `dls()` fills the cells in order; when it reaches the limit without filling the matrix, it returns (cutoff).
3. For each cell the values 1..n are tried; a value is accepted only if it is not already in the row or column.
4. If no value works, the cell is cleared (**backtrack**) and the next value is tried in the previous cell.
5. When the limit reaches n², DLS finds the solution.
6. The result is printed to the terminal and automatically saved to `results.txt` (overwritten on every run, so it keeps only the latest n).

## 6. Results (n = 5)

```
1 2 3 4 5
2 1 4 5 3
3 4 5 1 2
4 5 2 3 1
5 3 1 2 4

Depth where the solution was found: 25
Total nodes (all iterations): 13505923
Time: ~25–45 s
Objective function f = 0
```

**Discussion:** IDDFS is optimal when the solution is at a shallow depth, but here all solutions are
at depth n². The iterations with limit 0..n²−1 therefore re-explore the tree for nothing: of the 13,505,923 nodes, 13,505,885 come
from these iterations and only 38 from the last one. For n = 3 and n = 4 the solution appears immediately, while for n = 6
the program did not finish within 120 s. For this problem, plain DFS would be faster.
