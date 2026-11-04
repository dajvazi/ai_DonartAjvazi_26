# 1. Social Golfers Problem – DFS with Backtracking

## 1. Problem model
32 golfers play once a week in **g = 8 groups** of **p = 4** players (n = g × p = 32).
The goal is the maximum number of weeks **w** during which no pair of players plays in the same group more than once.

The problem is modelled as a **Constraint Satisfaction Problem (CSP)**: for a given *w* we look for an assignment
of values that satisfies all constraints, while the optimization version looks for the maximum *w*.

**Upper bound:** each week a player meets 3 new players, and there are 31 other players in total:

  w ≤ ⌊(n − 1) / (p − 1)⌋ = ⌊31 / 3⌋ = **10 weeks**

(The pairs give the same result: C(32,2) = 496 pairs, each week covers 8 · C(4,2) = 48 → ⌊496/48⌋ = 10.)

## 2. Problem representation

| Element | Description |
|---|---|
| **Variables** | `x[j][g][s]` – the player in week *j*, group *g*, position *s* (j = 1..w, g = 1..8, s = 1..4) |
| **Domain** | D = {0, 1, …, 31} |
| **Constraint 1** | Each week is a partition: every player appears exactly once per week |
| **Constraint 2** | For every pair (a, b): the number of weeks in which a and b share a group is ≤ 1 |
| **State** | The partial schedule (the weeks assigned so far) |
| **Initial state** | The empty schedule |
| **Action** | Add a valid week to the schedule |
| **Goal test** | The schedule has *w* weeks and f = 0 |

**Representation used in the implementation.** Players are 5-bit numbers. A week is defined by a
*key* {a, b, a⊕b} (⊕ = XOR), and its groups are {x, x⊕a, x⊕b, x⊕a⊕b}. Two players x, y are together
⇔ x⊕y ∈ key. Therefore two weeks share no pair ⇔ their keys are disjoint.
Each week is thus one variable with a **domain of 155 keys**, and constraint 2 simply becomes
"the chosen keys share no number". Constraint 1 is satisfied automatically by the construction.

## 3. Objective function

  f(schedule) = Σ₍a<b₎ max(0, meetings(a, b) − 1)

where meetings(a, b) is the number of weeks in which a and b are in the same group.

- f = 0 ⇔ the schedule is valid.
- Optimization problem: **max w** subject to f = 0.

## 4. Landscape (search space)

| Representation | Size |
|---|---|
| Possible partitions for one week: 32! / ((4!)⁸ · 8!) | ≈ 5.9 × 10¹⁹ |
| Naive variable assignments for one week: 32³² | ≈ 1.5 × 10⁴⁸ |
| 9 weeks, direct representation: (5.9 × 10¹⁹)⁹ | ≈ 9 × 10¹⁷⁷ |
| 9 weeks with keys (unordered): C(155, 9) | ≈ 1.1 × 10¹⁴ |

The landscape is very large and "flat": most schedules have f > 0 and solutions are rare.
The key representation and **symmetry breaking** (weeks are chosen in increasing key order, with no permutations)
reduce the space by more than 160 orders of magnitude.

## 5. Implementation – DFS with Backtracking (`golf.py`)

1. The 155 keys (the domain) are generated.
2. `dfs()` adds weeks one at a time (depth = number of weeks).
3. Before a key is added, the program checks whether it shares a number with the keys already used;
   if it does, the branch is **pruned**.
4. If a state cannot be extended, the last week is removed (**backtrack**) and the next key is tried.
5. Finally, the objective function is computed on the actual player schedule, and each week is checked to be a valid partition.
6. The result is printed to the terminal and automatically saved to `results.txt`.

## 6. Results

```
Weeks found: 9
Theoretical bound: 10 weeks
Nodes visited: 409
Time: < 0.05 s
Valid partition every week: True
Objective function f = 0
```
The full schedule is in `results.txt`.

**Answer:** The theoretical maximum is **10 weeks**, and such a solution exists. The DFS with Backtracking program finds **9** valid **weeks**, which is the maximum for the XOR key representation.

**Discussion:**
- `golf.py` stops as soon as it finds 9 weeks. An exhaustive search with a separate script showed that no 10 of the 155 keys are pairwise disjoint.
  The 10-week solution exists (Shen 1996, Aguado), but it requires a mathematical construction rather than an uninformed search over these keys.
- In a test with a naive DFS over players (slot by slot), week 5 was reached in about 0.002 s, while week 6 was not found within 60 s.
  This shows that in uninformed search the **choice of representation** is decisive.
