"""Re-runs every worked example and activity answer that can be computed.

Run:  python tools/check_examples.py
Each line prints the topic, what is checked, and the computed result, so a
reviewer can compare it with the Markdown. Uses only the Python standard library.
"""
import math, sqlite3
from collections import deque

def show(topic, what, result):
    print(f"[{topic}] {what}: {result}")

# ---------- Topic 01: round-robin scheduling (quantum 2 ms)
def round_robin(procs, q=2):
    queue, t, rem, done = deque(p for p, _ in procs), 0, dict(procs), []
    while queue:
        p = queue.popleft(); run = min(q, rem[p]); t += run; rem[p] -= run
        if rem[p]: queue.append(p)
        else: done.append((p, t))
    return done
show("01", "worked example finish times", round_robin([("Music", 3), ("Browser", 5), ("Editor", 2)]))
show("01", "activity 3 finish times", round_robin([("Game", 4), ("Chat", 1), ("Upload", 3)]))

# ---------- Topic 02: program outputs
total = 0
for n in [4, 7, 2]:
    if n > 3: total += n
show("02", "worked example output", total)
show("02", "activity 1 (== 0 / == 1)", (sum(1 for i in range(1, 6) if i % 2 == 0), sum(1 for i in range(1, 6) if i % 2 == 1)))
x, out = 10, []
while x > 1:
    x //= 2; out.append(x)
show("02", "activity 2 output", out)
show("02", "activity 3 buggy / fixed", (sum(n for n in [4, 7, 2] if n > 5), sum(n for n in [4, 7, 2] if n < 5)))

# ---------- Topic 04: SQL on the Students table
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE Students(student_id INTEGER PRIMARY KEY, name TEXT, major TEXT, year INTEGER, gpa REAL);
INSERT INTO Students VALUES (101,'Anu','Computer Science',1,3.6),(102,'Bat','Economics',2,3.1),
(103,'Chen','Computer Science',2,3.9),(104,'Dana','Design',1,3.4),(105,'Erdene','Economics',1,2.8),
(106,'Fatima','Computer Science',3,3.2);
CREATE TABLE Courses(course_id TEXT PRIMARY KEY, title TEXT, credits INTEGER);
INSERT INTO Courses VALUES ('CS101','Foundations of CS & AI',3),('EC110','Intro to Economics',3),('DS120','Visual Design',2);
CREATE TABLE Enrolments(student_id INTEGER, course_id TEXT);
INSERT INTO Enrolments VALUES (101,'CS101'),(102,'EC110'),(103,'CS101'),(104,'DS120'),(104,'CS101'),(105,'EC110'),(106,'CS101');
""")
for q in ["SELECT name, gpa FROM Students WHERE major = 'Computer Science' ORDER BY gpa DESC",
          "SELECT name FROM Students WHERE year = 1",
          "SELECT name, major FROM Students WHERE gpa >= 3.5",
          "SELECT name FROM Students WHERE major = 'Economics' AND year = 1",
          "SELECT * FROM Students WHERE major = 'Design' OR gpa < 3.0",
          "SELECT name, gpa FROM Students ORDER BY gpa ASC",
          "SELECT name FROM Students WHERE year = 2",
          "SELECT s.name FROM Students s JOIN Enrolments e ON s.student_id = e.student_id WHERE e.course_id = 'CS101'",
          "SELECT c.title FROM Enrolments e JOIN Courses c ON c.course_id = e.course_id WHERE e.student_id = 104"]:
    show("04", q, db.execute(q).fetchall())

# ---------- Topic 05: searching, sorting, recursion
def binary_search_trace(items, target):
    low, high, steps = 0, len(items) - 1, []
    while low <= high:
        mid = (low + high) // 2; steps.append((low, high, mid, items[mid]))
        if items[mid] == target: return steps, mid
        if items[mid] < target: low = mid + 1
        else: high = mid - 1
    return steps, -1
L = [3, 8, 12, 19, 25, 31, 40, 47]
for t in (31, 8, 10): show("05", f"binary search for {t} (low, high, mid, value)", binary_search_trace(L, t))
def bubble_passes(a):
    a, passes = list(a), []
    for p in range(len(a) - 1):
        swaps = 0
        for i in range(len(a) - 1 - p):
            if a[i] > a[i + 1]: a[i], a[i + 1] = a[i + 1], a[i]; swaps += 1
        passes.append((list(a), swaps))
        if swaps == 0: break
    return passes
show("05", "bubble sort [5,2,9,1,6]", bubble_passes([5, 2, 9, 1, 6]))
show("05", "bubble sort [4,3,1,2]", bubble_passes([4, 3, 1, 2]))
a, steps = [29, 10, 14, 37, 13], []
for i in range(len(a) - 1):
    m = min(range(i, len(a)), key=a.__getitem__); a[i], a[m] = a[m], a[i]; steps.append(list(a))
show("05", "selection sort steps", steps)
fact = lambda n: 1 if n <= 1 else n * fact(n - 1)
sum_to = lambda n: 0 if n == 0 else n + sum_to(n - 1)
show("05", "factorial(4), factorial(5), sum_to(4)", (fact(4), fact(5), sum_to(4)))
show("05", "binary search worst-case checks", {n: math.floor(math.log2(n)) + 1 for n in (8, 1000, 10**6, 10**9)})
show("05", "bubble comparisons n(n-1)/2 for 10 and 1000", (10 * 9 // 2, 1000 * 999 // 2))

# ---------- Topic 06: stack, queue, binary search tree
st, popped = [], []
for op in ["push 5", "push 8", "pop", "push 2", "push 7", "pop", "pop"]:
    if op == "pop": popped.append(st.pop())
    else: st.append(int(op.split()[1]))
show("06", "stack final / popped", (st, popped))
qu = deque()
for op in ["enq Anu", "enq Bat", "deq", "enq Chen", "enq Dana", "deq"]:
    qu.popleft() if op == "deq" else qu.append(op.split()[1])
show("06", "queue still waiting", list(qu))
tree = {}
def insert(k, node=50):
    if node is None: return
    side = "L" if k < node else "R"
    child = tree.get((node, side))
    if child is None: tree[(node, side)] = k
    else: insert(k, child)
for k in [30, 70, 20, 40, 60, 80, 35]: insert(k)
def path(k, node=50, p=None):
    p = (p or []) + [node]
    if node == k: return p, True
    child = tree.get((node, "L" if k < node else "R"))
    return (p, False) if child is None else path(k, child, p)
show("06", "BST search 60, 40, 65", [path(60), path(40), path(65)])
show("06", "35 inserted as left child of 40", tree.get((40, "L")) == 35)

# ---------- Topic 10 and 13: forward chaining
def forward(rules, facts):
    facts, fired = list(facts), []
    while True:
        for name, conds, concl in rules:
            if all(c in facts for c in conds) and concl not in facts:
                facts.append(concl); fired.append(name); break
        else: return fired, facts[len(facts) - len(fired):]
LAPTOP = [("R1", ["power light is off", "charger is plugged in"], "no power reaches the laptop"),
          ("R2", ["no power reaches the laptop"], "suspect charger or battery"),
          ("R3", ["suspect charger or battery", "another charger works"], "charger is faulty"),
          ("R4", ["suspect charger or battery", "another charger does not work"], "battery is faulty"),
          ("R5", ["power light is on", "screen is black"], "screen or display problem"),
          ("R6", ["charger is faulty"], "advice: replace the charger"),
          ("R7", ["battery is faulty"], "advice: replace the battery")]
show("10", "worked example", forward(LAPTOP, ["screen is black", "power light is off", "charger is plugged in", "another charger works"]))
show("10", "activity 1", forward(LAPTOP, ["screen is black", "power light is on"]))
show("10", "activity 3 (forward check)", forward(LAPTOP, ["power light is off", "charger is plugged in", "another charger does not work"]))
STUDY = [("R1", ["exam more than 3 days away", "topic is new"], "plan: spaced study"),
         ("R2", ["exam within 3 days", "topic is familiar"], "plan: final review"),
         ("R3", ["exam within 3 days", "topic is new"], "plan: focus on key points"),
         ("R4", ["plan: spaced study", "learner likes diagrams"], "advice: concept map"),
         ("R5", ["plan: final review"], "advice: practice questions"),
         ("R6", ["plan: focus on key points", "studying with friends"], "advice: teach each other")]
show("13", "worked example", forward(STUDY, ["exam more than 3 days away", "topic is new", "learner likes diagrams"]))
show("13", "activity 1 (gap)", forward(STUDY, ["exam within 3 days", "topic is new", "studying alone"]))
R7 = ("R7", ["plan: focus on key points", "studying alone"], "advice: one-page summary")
show("13", "activity 2 with R7", forward(STUDY + [R7], ["exam within 3 days", "topic is new", "studying alone"]))
show("13", "activity 3", forward(STUDY, ["exam within 3 days", "topic is familiar"]))

# ---------- Topic 11: BFS and DFS with alphabetical tie-break
def graph(edges):
    g = {}
    for a, b in edges: g.setdefault(a, set()).add(b); g.setdefault(b, set()).add(a)
    return g
def bfs(g, s, goal):
    q, par, order = deque([s]), {s: None}, []
    while q:
        n = q.popleft(); order.append(n)
        if n == goal: break
        for m in sorted(g[n]):
            if m not in par: par[m] = n; q.append(m)
    p, x = [], goal
    while x: p.append(x); x = par[x]
    return order, p[::-1]
def dfs(g, n, goal, seen=None, path=None):
    seen, path = (seen or []) + [n], (path or []) + [n]
    if n == goal: return seen, path
    for m in sorted(g[n]):
        if m not in seen:
            r = dfs(g, m, goal, seen, path)
            if r[1][-1] == goal: return r
            seen = r[0]
    return seen, path[:-1] or path
G1 = graph([("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","F"),("E","F")])
G2 = graph([("S","A"),("S","B"),("A","C"),("A","D"),("B","G"),("C","D"),("D","G")])
show("11", "map 1 BFS (order, path)", bfs(G1, "A", "F")); show("11", "map 1 DFS (order, path)", dfs(G1, "A", "F"))
show("11", "map 2 BFS (order, path)", bfs(G2, "S", "G")); show("11", "map 2 DFS (order, path)", dfs(G2, "S", "G"))

# ---------- Topic 12: keyword chatbot
def bot(msg, rules):
    for name, kws in rules:
        if any(k in msg.lower() for k in kws): return name
    return "Default"
CANTEEN = [("C1", ["open", "hours"]), ("C2", ["menu", "food"]), ("C3", ["pay", "card"])]
LIBRARY = [("L1", ["borrow", "loan"]), ("L2", ["open", "hours"]), ("L3", ["print"])]
for m in ["What are your opening hours?", "Can I pay by card?", "Is the food open to visitors?",
          "I don't want to pay by card, can I use cash?"]: show("12", m, bot(m, CANTEEN))
for m in ["How long can I keep a book?", "Is the printer open on Sunday?"]: show("12", m, bot(m, LIBRARY))

# ---------- Topic 13 quiz Q2
x = 2
for i in range(3): x *= 2
show("13", "quiz Q2 output", x)

# ---------- Topic 08: truth tables (T/F rows in the order TT, TF, FT, FF)
rows = [(True, True), (True, False), (False, True), (False, False)]
tf = lambda v: "T" if v else "F"
show("08", "P AND Q / P OR Q / NOT P / IF P THEN Q",
     ["".join(tf(v) for v in (p and q, p or q, not p, (not p) or q)) for p, q in rows])
show("08", "activity 3: P AND (NOT Q)", [tf(p and not q) for p, q in rows])
