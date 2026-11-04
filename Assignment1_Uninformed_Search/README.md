# First Semester Assignment – Uninformed Search Techniques

**Student:** Donart Ajvazi

**Requirement:** Python 3 (no additional libraries)

## Structure

```
Assignment1_Uninformed_Search/
├── README.md
├── 1_Social_Golfers/   README.md · golf.py   · results.txt   (DFS + Backtracking)
├── 2_Sudoku/           README.md · sudoku.py · results.txt   (BFS + Backtracking)
├── 3_Latin_Square/     README.md · latin.py  · results.txt   (IDDFS + Backtracking)
└── 4_Search_Trees/     README.md · *.drawio  · *.png
```

Each README in folders 1–3 contains: the model, the representation (variables, domain, constraints),
the objective function, the landscape, the implementation and the results.

## Running

| Task | Algorithm | Command |
|---|---|---|
| 1. Social Golfers | DFS + Backtracking | `python 1_Social_Golfers/golf.py` |
| 2. Sudoku | BFS + Backtracking | `python 2_Sudoku/sudoku.py` |
| 3. Latin Square | IDDFS + Backtracking | `python 3_Latin_Square/latin.py 5` |
| 4. Search Trees | – | open the `.drawio` files at https://app.diagrams.net or view the `.png` files |

Each program prints its result to the terminal and automatically saves it to `results.txt` in its own folder.
The times below depend on the computer.

## Summary of results

| Task | Result | f |
|---|---|---|
| Social Golfers | 9 weeks with no repeated pair (409 nodes, < 0.05 s); the theoretical maximum is 10 weeks | 0 |
| Sudoku | Easy, Medium and Hard solved (< 1 s in total) | 0 |
| Latin Square | 5×5 Latin square (depth 25, ~25–45 s) | 0 |
| Search Trees | 3 trees: 8-Puzzle, Missionaries & Cannibals, Rotating Workforce | – |
