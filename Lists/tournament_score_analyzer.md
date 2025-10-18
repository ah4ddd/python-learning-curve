```python
players = []
scores = []

num_players = int(input("Number of players? "))
num_rounds = int(input("Number of rounds? "))

for p in range(num_players):
    name = input(f"Enter name of player {p+1}: ")
    players.append(name)

    player_scores = []
    for r in range(num_rounds):
        score = int(input(f"Score for {name} in round {r+1}: "))
        player_scores.append(score)

    scores.append(player_scores)

max_score = -float('inf')
min_score = float('inf')
max_player = ""
min_player = ""
max_round = 0
min_round = 0

for i in range(num_players):
    for j in range(num_rounds):
        score = scores[i][j]

        if score > max_score:
            max_score = score
            max_player = players[i]
            max_round = j+1

        if score < min_score:
            min_score = score
            min_player = players[i]
            min_round = j+1

print(f"\nOverall Highest Score: {max_score} by {max_player} in Round {max_round}")
print(f"Overall Lowest Score: {min_score} by {min_player} in Round {min_round}")

print("\nTop performer per round:")
for r in range(num_rounds):
    top_score = -float('inf')
    top_player = ""
    for i in range(num_players):
        if scores[i][r] > top_score:
            top_score = scores[i][r]
            top_player = players[i]
    print(f"Round {r+1}: {top_player} with {top_score} points")
```


---

# Full program (the Tournament Score Analyzer)

```python
players = []
scores = []

num_players = int(input("Number of players? "))
num_rounds = int(input("Number of rounds? "))

for p in range(num_players):
    name = input(f"Enter name of player {p+1}: ")
    players.append(name)

    player_scores = []
    for r in range(num_rounds):
        score = int(input(f"Score for {name} in round {r+1}: "))
        player_scores.append(score)

    scores.append(player_scores)

max_score = -float('inf')
min_score = float('inf')
max_player = ""
min_player = ""
max_round = 0
min_round = 0

for i in range(num_players):
    for j in range(num_rounds):
        score = scores[i][j]
        if score > max_score:
            max_score = score
            max_player = players[i]
            max_round = j+1
        if score < min_score:
            min_score = score
            min_player = players[i]
            min_round = j+1

print(f"\nOverall Highest Score: {max_score} by {max_player} in Round {max_round}")
print(f"Overall Lowest Score: {min_score} by {min_player} in Round {min_round}")

print("\nTop performer per round:")
for r in range(num_rounds):
    top_score = -float('inf')
    top_player = ""
    for i in range(num_players):
        if scores[i][r] > top_score:
            top_score = scores[i][r]
            top_player = players[i]
    print(f"Round {r+1}: {top_player} with {top_score} points")
```

---

# Now: line-by-line, word-by-word explanation

I’ll show a small chunk, then explain **every single token** that matters.

---

### 1)

```python
players = []
```

* `players` — a variable name. We'll use it to store player names.
* `=` — assignment. Put the value on the right into the variable on the left.
* `[]` — an **empty list** (no items yet). Lists hold ordered items (0th, 1st, 2nd...).
* Result: `players` now points to an empty list `[]`.

---

### 2)

```python
scores = []
```

* `scores` — variable for storing scores.
* `[]` — empty list again.
* But **we will use `scores` as a list of lists**. Each element of `scores` will be a list of that player's round scores.
* Example final shape: `scores = [ [p1r1, p1r2, ...], [p2r1, p2r2, ...], ... ]`.

---

### 3)

```python
num_players = int(input("Number of players? "))
```

Breakdown:

* `input("Number of players? ")` — show the text `Number of players? ` on screen, pause, and wait for keyboard input. **Input returns a string**.

  * If user types `3` and presses Enter, `input(...)` returns the string `"3"`.
* `int(...)` — converts a string to an integer (number). `int("3")` → `3` (as number).

  * If user types a non-number like `abc`, `int()` raises `ValueError` (program crashes unless caught).
* `num_players` — variable storing that integer number of players.

So after this line: `num_players` is an integer like `2`, `3`, etc.

---

### 4)

```python
num_rounds = int(input("Number of rounds? "))
```

Same as above, but for rounds per player. `num_rounds` is an integer.

---

### 5) Outer loop start

```python
for p in range(num_players):
```

* `for` — start a loop.
* `p` — loop variable (will take values 0,1,2,...).
* `range(num_players)` — generates numbers from `0` to `num_players - 1`.

  * If `num_players` is `3`, `range(3)` gives `0,1,2`.
* The loop body (indented block that follows) runs once for each player.

**Important:** we use 0-based counting in code. `p` refers to the current player index.

---

### 6)

```python
    name = input(f"Enter name of player {p+1}: ")
```

* `f"Enter name of player {p+1}: "` — an f-string. `{p+1}` is replaced by the value `p+1`.

  * We use `p+1` because humans count players from 1, but our code index `p` starts at 0.
* `input(...)` displays that prompt and reads a string typed by user.
* `name` receives the typed string (like `"Alice"`).

---

### 7)

```python
    players.append(name)
```

* `players.append(...)` — **call** the list method `append` to add the `name` to the end of `players`.
* After this, `players` grows. Example: `["Alice"]`, then `["Alice", "Bob"]`, etc.

---

### 8)

```python
    player_scores = []
```

* `player_scores` — temporary list for this player's round scores.
* `[]` — empty list. We'll fill it with `num_rounds` integers.

---

### 9) Inner loop start

```python
    for r in range(num_rounds):
```

* `r` — loop variable for round index (0..num_rounds-1).
* This loop repeats `num_rounds` times for the current player.

---

### 10)

```python
        score = int(input(f"Score for {name} in round {r+1}: "))
```

* `f"Score for {name} in round {r+1}: "` → builds prompt like: `Score for Alice in round 1: `
* `input(...)` reads a string typed by user.
* `int(...)` converts that string to an integer (`score`).

  * Again, bad input (non-number) causes `ValueError`.
* `score` now holds the numeric score for this player in this round.

---

### 11)

```python
        player_scores.append(score)
```

* Add this `score` to the current player's `player_scores` list.
* After all rounds, `player_scores` might look like `[10, 5, 7]` for 3 rounds.

---

### 12)

```python
    scores.append(player_scores)
```

* After the inner loop finishes (we collected all rounds for this player), we append the full `player_scores` list into `scores`.
* So `scores` becomes a list of lists. Example after two players:

  ```
  scores = [
    [10, 5, 7],  # player 0
    [6, 12, 8]   # player 1
  ]
  ```

---

### 13)

```python
max_score = -float('inf')
min_score = float('inf')
```

* `float('inf')` is Python's positive infinity (a very big number).
* `-float('inf')` is negative infinity (a very small number).
* We initialize `max_score` to negative infinity so any real score will be larger and will replace it.
* We initialize `min_score` to positive infinity so any real score will be smaller and will replace it.

This is a safe way to start so the first checked score becomes both max and min initially.

---

### 14)

```python
max_player = ""
min_player = ""
max_round = 0
min_round = 0
```

* `max_player` / `min_player` — strings to store the name of the player who has the extreme score.
* `max_round` / `min_round` — integers storing which round (we’ll store `j+1` so it’s human readable).
* Start as empty / zero; they will be set when we find scores.

---

### 15) Nested loop to find overall extremes

```python
for i in range(num_players):
    for j in range(num_rounds):
        score = scores[i][j]
```

* Outer loop: `i` iterates players by index (0..num_players-1).
* Inner loop: `j` iterates rounds by index (0..num_rounds-1).
* `scores[i][j]` — **indexing a list of lists**:

  * `scores[i]` → list of player `i` scores.
  * `scores[i][j]` → score of player `i` in round `j`.
* `score` holds the current numeric score we're examining.

---

### 16) Compare for max

```python
        if score > max_score:
            max_score = score
            max_player = players[i]
            max_round = j+1
```

* `if score > max_score:` — check if this score is strictly greater than our current recorded max.
* If true:

  * `max_score = score` — update the numeric max.
  * `max_player = players[i]` — get the player's name (because `players` list stores names in same order).
  * `max_round = j+1` — store the human-friendly round number (add 1 because `j` starts at 0).

---

### 17) Compare for min

```python
        if score < min_score:
            min_score = score
            min_player = players[i]
            min_round = j+1
```

* Same logic but for the minimum. If this score is lower than current min, update min vars.

**Note:** both `if` blocks are separate — the same `score` can update both `max_score` and `min_score` at first iteration.

---

### 18) Print extremes

```python
print(f"\nOverall Highest Score: {max_score} by {max_player} in Round {max_round}")
print(f"Overall Lowest Score: {min_score} by {min_player} in Round {min_round}")
```

* `f"...{var}..."` — f-strings: they fill in variable values into the string.
* `\n` — newline, makes formatting cleaner.
* Shows the final results.

---

### 19) Top performer per round

```python
print("\nTop performer per round:")
for r in range(num_rounds):
    top_score = -float('inf')
    top_player = ""
    for i in range(num_players):
        if scores[i][r] > top_score:
            top_score = scores[i][r]
            top_player = players[i]
    print(f"Round {r+1}: {top_player} with {top_score} points")
```

* For each round `r` (0..num_rounds-1):

  * Reset `top_score` to negative infinity (so first player’s score becomes top_score).
  * Loop over every player `i` and check `scores[i][r]` (player i's score in round r).
  * If that score is bigger than current `top_score`, update `top_score` and `top_player`.
  * After checking all players, print the winner for that round.

---

# Now: concrete run-through (trace) with real inputs — **line by line memory trace**

I’ll use this sample input so you can watch variables change:

* `num_players` = 2
* `num_rounds` = 3
* Player names & scores typed:

  * Player 1: `Alice` scores `10`, `5`, `7`
  * Player 2: `Bob`   scores `6`, `12`, `8`

Start: `players = []`, `scores = []`.

**After reading numbers**

* `num_players = 2`
* `num_rounds = 3`

**First outer loop iteration (p = 0):**

* Prompt: `Enter name of player 1:` user types `Alice` → `name = "Alice"`
* `players.append(name)` → `players = ["Alice"]`
* `player_scores = []`

Inner loop for Alice (`r` goes 0,1,2):

* r = 0 → prompt `Score for Alice in round 1:` user types `10` → `score = 10`

  * `player_scores.append(10)` → `player_scores = [10]`
* r = 1 → prompt `Score for Alice in round 2:` user types `5` → `score = 5`

  * `player_scores.append(5)` → `player_scores = [10, 5]`
* r = 2 → `Score for Alice in round 3:` user types `7` → `player_scores.append(7)` → `[10,5,7]`

After inner loop: `scores.append(player_scores)` → `scores = [[10,5,7]]`

**Second outer loop iteration (p = 1):**

* `Enter name of player 2:` user types `Bob` → `players = ["Alice", "Bob"]`
* `player_scores = []`
* r = 0 → `Score for Bob in round 1:` user types `6` → player_scores `[6]`
* r = 1 → `12` → player_scores `[6,12]`
* r = 2 → `8` → player_scores `[6,12,8]`
* append → `scores = [[10,5,7], [6,12,8]]`

**After input phase memory**

```
players = ["Alice", "Bob"]
scores = [
  [10, 5, 7],   # scores[0]
  [ 6,12, 8]    # scores[1]
]
```

**Initialize extremes**

```
max_score = -inf
min_score = +inf
max_player = ""
min_player = ""
max_round = 0
min_round = 0
```

**Now nested loops to find overall extremes**

We iterate `i` in `0..1`, and `j` in `0..2`.

* i=0, j=0 → score = scores[0][0] = 10

  * Is 10 > max_score (-inf)? yes → max_score=10, max_player="Alice", max_round = 0+1 = 1
  * Is 10 < min_score (+inf)? yes → min_score=10, min_player="Alice", min_round = 1
* i=0, j=1 → score = scores[0][1] = 5

  * Is 5 > max_score (10)? no → skip
  * Is 5 < min_score (10)? yes → min_score=5, min_player="Alice", min_round = 2
* i=0, j=2 → score = 7

  * 7 > max_score (10)? no
  * 7 < min_score (5)? no
* i=1, j=0 → score = 6

  * 6 > 10? no
  * 6 < 5? no
* i=1, j=1 → score = 12

  * 12 > 10? yes → max_score=12, max_player="Bob", max_round = 1+1 = 2
  * 12 < 5? no
* i=1, j=2 → score = 8

  * 8 > 12? no
  * 8 < 5? no

**After nested loop**

* `max_score = 12`, `max_player = "Bob"`, `max_round = 2`
* `min_score = 5`, `min_player = "Alice"`, `min_round = 2`

Printed:

```
Overall Highest Score: 12 by Bob in Round 2
Overall Lowest Score: 5 by Alice in Round 2
```

**Top performer per round loop**

* r = 0:

  * top_score = -inf
  * i=0 → scores[0][0] = 10 → 10 > -inf → top_score=10, top_player="Alice"
  * i=1 → scores[1][0] = 6  → 6 > 10? no
  * print: `Round 1: Alice with 10 points`
* r = 1:

  * top_score = -inf
  * i=0 → scores[0][1] = 5  → top_score=5, top_player="Alice"
  * i=1 → scores[1][1] = 12 → 12 > 5 → top_score=12, top_player="Bob"
  * print: `Round 2: Bob with 12 points`
* r = 2:

  * top_score = -inf
  * i=0 → 7 → top_score=7, top_player="Alice"
  * i=1 → 8 → 8 > 7 → top_score=8, top_player="Bob"
  * print: `Round 3: Bob with 8 points`

Final printed round winners:

```
Round 1: Alice with 10 points
Round 2: Bob with 12 points
Round 3: Bob with 8 points
```

---

# Extra tiny details & gotchas (word-by-word)

* `input()` always returns a **string**. Use `int()` to convert to number.
* `int("3")` -> `3`. `int("3.5")` raises `ValueError`. `int("abc")` raises `ValueError`.
* `range(n)` counts `0` to `n-1`. If you want human numbering, add `+1` when printing.
* `scores[i][j]` — first `[i]` picks player row, second `[j]` picks round column.
* `-float('inf')` and `float('inf')` are just safe initial extremes.
* `if score > max_score:` uses strict `>` (not `>=`). If you want to capture ties differently, logic changes.
* `append()` modifies the list **in place** (it does not return a new list).
* Loops are nested; total checks = `num_players * num_rounds`.
* Complexity: O(P * R), where P=num_players, R=num_rounds. For small tournaments that's fine.

---

# Short checklist so you can code this without surprises

* Convert inputs with `int()` and **only enter numbers** for scores and counts.
* Names are strings — you can use spaces, special chars.
* If you expect bad input, wrap conversions in `try/except ValueError` (we did not do that here).
* If multiple players tie for top score and you want all of them, you must collect them (this code only records the first one encountered).

---

Let’s walk through this slowly and concretely, no fog.
I’ll literally **show you the lists in memory** and then track exactly what every line in that block is doing to them.

---

### Suppose this is what exists in memory right before that code runs

```python
players = ["Ahad", "Leo", "Maya"]

scores = [
    [15, 25, 10],   # Ahad's scores (round1, round2, round3)
    [30, 22, 18],   # Leo's scores
    [12, 50, 45]    # Maya's scores
]

num_players = 3
num_rounds = 3
```

Think of `scores` as a **table of numbers**:

```
          round0  round1  round2
Ahad  ->   15      25      10
Leo   ->   30      22      18
Maya  ->   12      50      45
```

* `scores[0]` → `[15,25,10]`  → Ahad’s row
* `scores[1]` → `[30,22,18]`  → Leo’s row
* `scores[2]` → `[12,50,45]`  → Maya’s row
* `scores[i][r]` → look inside the table: row *i*, column *r*.

---

### Now the code

```python
for r in range(num_rounds):

    top_score = -float('inf')
    top_player = ""

    for i in range(num_players):
        if scores[i][r] > top_score:
            top_score = scores[i][r]
            top_player = players[i]

    print(f"Round {r+1}: {top_player} with {top_score} points")
```

Let’s visualize **how it moves through memory**.

---

#### 1️⃣ Outer loop: `for r in range(num_rounds)`

* `range(num_rounds)` → `[0,1,2]`
* So the variable `r` will be 0, then 1, then 2.
* You can think of `r` as a pointer moving **column by column** across the table.

```
First outer loop → r = 0  (column 0)
Second outer loop → r = 1  (column 1)
Third outer loop → r = 2   (column 2)
```

---

#### 2️⃣ Each round starts with reset

```python
top_score = -float('inf')
top_player = ""
```

We clear out any leftover data so that the next round starts fresh.

`-float('inf')` just means “start lower than any real number” so the first real score will always replace it.

---

#### 3️⃣ Inner loop: `for i in range(num_players)`

* `range(num_players)` → `[0,1,2]`
* So `i` will be 0 → 1 → 2 inside each round.
* You can think of `i` as a pointer moving **row by row** down the table.

When `r=0` (Round 1):

| i | Expression     | What it points to | Value |
| - | -------------- | ----------------- | ----- |
| 0 | `scores[0][0]` | Ahad, Round 1     | 15    |
| 1 | `scores[1][0]` | Leo, Round 1      | 30    |
| 2 | `scores[2][0]` | Maya, Round 1     | 12    |

That’s how it “uses the list”: the first index chooses the player’s row, the second chooses which round inside that player’s row.

---

#### 4️⃣ The comparison

```python
if scores[i][r] > top_score:
    top_score = scores[i][r]
    top_player = players[i]
```

**What happens inside Round 1 (`r=0`):**

1. `i=0`:

   * `scores[0][0] = 15`
   * Compare `15 > -∞` → True
   * Update → `top_score = 15`, `top_player = "Ahad"`

2. `i=1`:

   * `scores[1][0] = 30`
   * Compare `30 > 15` → True
   * Update → `top_score = 30`, `top_player = "Leo"`

3. `i=2`:

   * `scores[2][0] = 12`
   * Compare `12 > 30` → False
   * Nothing changes.

When the inner loop finishes, we’ve scanned that whole column (Round 1) and found that Leo has the highest number.

---

#### 5️⃣ Print the result for that round

```python
print(f"Round {r+1}: {top_player} with {top_score} points")
```

Prints →
`Round 1: Leo with 30 points`

---

#### 6️⃣ Outer loop continues

Next outer iteration `r=1` (Round 2)

The inner loop repeats the same process, but this time it’s looking at **column 1** in each row:

| i | scores[i][1] | Player | Comparison                    |
| - | ------------ | ------ | ----------------------------- |
| 0 | 25           | Ahad   | 25 > -∞ → top=25, player=Ahad |
| 1 | 22           | Leo    | 22 > 25 ❌                     |
| 2 | 50           | Maya   | 50 > 25 ✅ top=50, player=Maya |

Result → `Round 2: Maya with 50 points`

Then again for `r=2` (Round 3) → Maya with 45 points.

---

### 🔍 The connection you were missing

You *do* see the lists being used here:

* `scores[i][r]` → accesses the score directly out of the nested list.
* `players[i]` → grabs the player’s name from the list of names.

So the code is literally pulling data from those two lists every time the inner loop runs.
No magic.
Just:

1. pick a round (`r`)
2. look through all players (`i`)
3. read from the two lists at those indexes.

---

### If you visualize it as coordinates

Imagine the table again with row/column coordinates:

```
          r=0   r=1   r=2
i=0 Ahad   15    25    10
i=1 Leo    30    22    18
i=2 Maya   12    50    45
```

* Outer loop (`r`) moves → right
* Inner loop (`i`) moves ↓ down
* `scores[i][r]` means → “go to row i, column r”

That’s literally how Python walks through the data and gets the correct numbers.

---

ASCII flowchart style, step by step, **top to bottom**, and visualize everything that happens behind the scenes

---

```python
START
 |
 |--> Initialize empty lists
 |       players = []
 |       scores = []
 |
 |--> Get number of players (num_players) and rounds (num_rounds)
 |
 |--> PLAYER LOOP (for p in range(num_players))
 |       |
 |       |--> Input player name
 |       |       name = input(...)
 |       |--> Append to players list
 |       |       players.append(name)
 |       |
 |       |--> Initialize empty player_scores list
 |       |       player_scores = []
 |       |
 |       |--> ROUND LOOP (for r in range(num_rounds))
 |       |       |
 |       |       |--> Input score for this player, this round
 |       |       |       score = int(input(...))
 |       |       |--> Append score to player_scores
 |       |       |       player_scores.append(score)
 |       |
 |       |--> Append completed player_scores to scores
 |               scores.append(player_scores)
 |
 |--> At this point:
 |       players = ["Ahad", "Leo", "Maya", ...]
 |       scores = [
 |           [15, 20, 18],  # Ahad's scores
 |           [30, 25, 28],  # Leo's scores
 |           [12, 14, 17],  # Maya's scores
 |           ...
 |       ]
 |
 |--> Initialize max/min trackers
 |       max_score = -float('inf')
 |       min_score = float('inf')
 |       max_player = ""
 |       min_player = ""
 |       max_round = 0
 |       min_round = 0
 |
 |--> FIND OVERALL MAX/MIN SCORES
 |       PLAYER LOOP (for i in range(num_players))
 |           |
 |           ROUND LOOP (for j in range(num_rounds))
 |               |
 |               |--> Get current score
 |               |       score = scores[i][j]
 |               |
 |               |--> Check if score > max_score
 |               |       If yes:
 |               |           max_score = score
 |               |           max_player = players[i]
 |               |           max_round = j+1
 |               |
 |               |--> Check if score < min_score
 |                       If yes:
 |                           min_score = score
 |                           min_player = players[i]
 |                           min_round = j+1
 |
 |--> Print Overall Highest and Lowest Scores
 |
 |--> TOP PERFORMER PER ROUND
 |       ROUND LOOP (for r in range(num_rounds))
 |           |
 |           |--> Reset top_score and top_player for this round
 |           |       top_score = -float('inf')
 |           |       top_player = ""
 |           |
 |           PLAYER LOOP (for i in range(num_players))
 |               |
 |               |--> Check if scores[i][r] > top_score
 |                       If yes:
 |                           top_score = scores[i][r]
 |                           top_player = players[i]
 |           |
 |           Print top player for this round
 |
END
```

---

### 💡 Behind-the-Scenes Walkthrough (Step-by-Step)

1. **Players and scores lists**

   * `players` stores the **names**.
   * `scores` stores a **list of scores for each player** → this is a 2D list.

2. **Nested loops to fill scores**

   * Outer loop = player by player.
   * Inner loop = round by round for that player.
   * By the end, `scores[i][j]` is the score of **player i in round j**.

3. **Max/min search**

   * Outer loop = all players.
   * Inner loop = all rounds.
   * Each `score = scores[i][j]` → checks against `max_score` and `min_score`.
   * **If condition triggers**, it updates `max_score` and **links that score to the player & round** via `max_player = players[i]` and `max_round = j+1`.

4. **Top performer per round**

   * Outer loop = round by round (r = 0 → first round, r = 1 → second round, etc.).
   * Reset `top_score` and `top_player` **for each round**.
   * Inner loop = iterate over all players for **that same round**.
   * Compare each player’s score for that round → update top_score and top_player.
   * Print after inner loop finishes → winner for that round is known.

---

### 🔑 Key Insights

* **Nested loops are essential** for 2D data: rows = players, columns = rounds.
* **`scores[i][r]`** = magic formula linking the **row (player)** and **column (round)**.
* **Updating player names** is done automatically when the score beats the current `top_score` or `max_score`.
* Resetting variables per round ensures no leftover data from previous rounds.

---

**properly visualized**, step by step — like a “pointer moving through a 2D grid” so you can literally see how `scores[i][r]` is being accessed in the top performer per round part.

Let’s assume 3 players and 3 rounds:

```python
Players: ["Ahad", "Leo", "Maya"]

Scores (2D list):
      Round 1  Round 2  Round 3
Ahad    15       20       18
Leo     30       25       28
Maya    12       14       17
```

---

### Step 1: Outer loop = Round by round


```python
for r in range(num_rounds):
    top_score = -inf
    top_player = ""
```

* `r = 0` → Round 1
* `r = 1` → Round 2
* `r = 2` → Round 3
* **We reset `top_score` and `top_player` for each round**, so previous round’s winner doesn’t interfere.

---

### Step 2: Inner loop = Iterate players

```python
for i in range(num_players):
    if scores[i][r] > top_score:
        top_score = scores[i][r]
        top_player = players[i]
```

* `i = 0` → Ahad
* `i = 1` → Leo
* `i = 2` → Maya

**Now visualize the pointer moving through the grid for Round 1 (r=0):**

```python
[Round 1 pointer → r=0]

Check Ahad: scores[0][0] = 15
   top_score = -inf → 15 > -inf → YES
   top_score = 15
   top_player = "Ahad"

Check Leo: scores[1][0] = 30
   top_score = 15 → 30 > 15 → YES
   top_score = 30
   top_player = "Leo"

Check Maya: scores[2][0] = 12
   top_score = 30 → 12 > 30 → NO
   top_score stays 30
   top_player stays "Leo"

Round 1 winner = Leo with 30 points
```

* ✅ The inner loop **checks all players for the same round**.
* ✅ The outer loop controls **which round we are checking**.
* After inner loop finishes, we print the winner.

---

### Step 3: Round 2 (r=1)

```python
Check Ahad: scores[0][1] = 20
   top_score = -inf → 20 > -inf → YES
   top_score = 20
   top_player = "Ahad"

Check Leo: scores[1][1] = 25
   top_score = 20 → 25 > 20 → YES
   top_score = 25
   top_player = "Leo"

Check Maya: scores[2][1] = 14
   top_score = 25 → 14 > 25 → NO
   top_score stays 25
   top_player stays "Leo"

Round 2 winner = Leo with 25 points
```

---

### Step 4: Round 3 (r=2)

```python
Check Ahad: scores[0][2] = 18
   top_score = -inf → 18 > -inf → YES
   top_score = 18
   top_player = "Ahad"

Check Leo: scores[1][2] = 28
   top_score = 18 → 28 > 18 → YES
   top_score = 28
   top_player = "Leo"

Check Maya: scores[2][2] = 17
   top_score = 28 → 17 > 28 → NO
   top_score stays 28
   top_player stays "Leo"

Round 3 winner = Leo with 28 points
```

---

### 🔑 Visualization Summary

* **Outer loop (r)** → Which round we are checking → locks the column.
* **Inner loop (i)** → Which player we are checking → moves down the rows of that column.
* `scores[i][r]` → Accesses the **cell at row i (player), column r (round)**.
* The `if` condition → decides whether to update the top_score and top_player.
* Once inner loop ends → we know the **winner of that round**.
* Then outer loop increments → move to next round → repeat.

---

### Quick ASCII Grid View (Pointer Example)

```
Scores Grid:
           R1  R2  R3
Ahad        ↑
Leo         ↑
Maya        ↑
```

* Round 1 → outer loop locks R1
* Inner loop → pointer goes down the column: Ahad → Leo → Maya
* Winner stored in top_player
* Round 2 → outer loop locks R2
* Inner loop → pointer goes down column R2: Ahad → Leo → Maya
* Winner stored in top_player
* Round 3 → same for column R3

---
