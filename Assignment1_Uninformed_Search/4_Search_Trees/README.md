# 4. Search Trees

The trees are in **draw.io** format (`.drawio`, open at https://app.diagrams.net) and exported as **PNG**.

Colors: yellow = start, blue = valid state, red = violates a constraint (pruned),
gray = repeated state, green = goal.

## 4a. 8-Puzzle (`8_puzzle.drawio`)
- **State:** a 3×3 grid with 8 tiles and one blank (`_`)
- **Start:** `1 2 3 / 4 _ 6 / 7 5 8`   **Goal:** `1 2 3 / 4 5 6 / 7 8 _`
- **Actions:** move the blank ↑ ↓ ← → (2–4 actions)
- **Space:** 9!/2 = 181,440 reachable states
- The tree shows levels 0–2 (BFS, no repeated states); the goal is reached at depth 2: ↓ then →.

## 4b. Missionaries and Cannibals (`missionaries_cannibals.drawio`)
- **State:** (M, K, B) – missionaries (M) and cannibals (K) on the left bank, B = boat position (L/R)
- **Start:** (3, 3, L)   **Goal:** (0, 0, R)
- **Actions:** the boat carries 1M, 2M, 1K, 2K or 1M+1K
- **Constraint:** on neither bank may cannibals outnumber missionaries (when missionaries are present)
- **Space:** 4 · 4 · 2 = 32 states; 20 of them satisfy the constraint, and 16 of those are reachable from the start
- The tree is built with BFS and shows all branches up to the goal: invalid and repeated states are pruned.
  The solution has **11 moves**: (3,3,L) → (3,1,R) → (3,2,L) → (3,0,R) → (3,1,L) → (1,1,R) → (2,2,L) → (0,2,R) → (0,3,L) → (0,1,R) → (1,1,L) → (0,0,R).

## 4c. Rotating Workforce Scheduling (`rotating_workforce.drawio`)
- **Instance:** 3 workers (P1, P2, P3), shifts **D** (day), **N** (night), **–** (rest)
- **Daily demand:** exactly 1 D and 1 N per day
- **Sequence constraint:** a D shift may not follow an N shift (N → D)
- **Rotating:** the weekly schedule is followed in rotation by the workers (P1 takes P2's week, etc.)
- **State:** the partial schedule; **action:** assign the shift of the next cell (P1 Day 1, P2 Day 1, P3 Day 1, P1 Day 2, …)
- **Space:** 3^(3·7) = 3²¹ ≈ 1.05 × 10¹⁰ assignments
- The tree shows the first two days: levels 1–2 are fully expanded, and beyond that one valid branch is expanded for each value of P1 on Day 1.
  Branches are pruned when a day has 2 D / 2 N, when D/N is not covered, or when N → D is violated.
- The green "Orar i plotë" ("complete schedule") nodes show a valid schedule for the 2 days displayed, not for all 7 days.
