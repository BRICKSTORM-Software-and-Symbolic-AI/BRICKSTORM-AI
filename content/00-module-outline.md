# Module Outline: Software and Symbolic AI

**Version:** V2.0 snapshot, 3 November 2026 (V1.0: 24 October 2026)  
**Module:** Chapter 3 (Software & Algorithms) and Chapter 4 (Symbolic AI), Foundations of CS & AI 2026

## Intended Learning Outcomes

After the whole module, a beginner can:

1. Explain system vs application software and what an operating system does.
2. Describe how programming languages, software engineering and databases support software development.
3. Carry out basic searching, sorting and recursive algorithms by hand and explain basic data structures.
4. Explain what Symbolic AI is and how it represents knowledge with logic, facts and rules.
5. Show step by step how a rule-based system and a search procedure reach a conclusion.
6. Discuss real-world uses, strengths and limits of Symbolic AI.

## Prerequisite Knowledge

Basic computer use (files, browsers, apps). No programming, logic or mathematics beyond secondary school. Each topic lists its own prerequisites, and every new term is defined where it first appears.

## Learning Sequence and Development Status

Status labels: **Outline only** (objectives and plan, no teaching text yet) · **Drafted** (full text with example, activity and answer, not yet reviewed) · **Checked** (reviewed by a second member) · **Needs revision**. A topic becomes "Checked" only when the review is recorded in the Stage 2 logs.

| # | Topic | Main worked example and activity | Learning outcome | Status |
|---|---|---|---|---|
| 01 | [Software Overview and OS](software-and-algorithms/01-software-overview-and-os.md) | Double-click walk-through; round-robin scheduling trace; sorting programs | 1 | Drafted V2.0 |
| 02 | [Programming Languages](software-and-algorithms/02-programming-languages.md) | Tracing a five-line program; predict the output; find the error | 2 | Drafted V2.0 |
| 03 | [Software Engineering](software-and-algorithms/03-software-engineering.md) | Study-timer app through the life cycle; which stage should have caught it | 2 | Drafted V2.0 |
| 04 | [Databases and SQL](software-and-algorithms/04-databases-and-sql.md) | Queries on a Students table; predict the rows | 2 | Drafted V2.0 |
| 05 | [Algorithms](software-and-algorithms/05-algorithms.md) | Binary search, bubble sort, recursion traced by hand | 3 | Drafted V2.0 |
| 06 | [Data Structures](software-and-algorithms/06-data-structures.md) | Back button as a stack; BST search; choosing structures | 3 | Drafted V2.0 |
| 07 | [Intro to Symbolic AI](symbolic-ai/07-intro-to-symbolic-ai.md) | Animal-guessing rules; classify AI systems | 4, 6 | Drafted V2.0 |
| 08 | [Logic and Reasoning](symbolic-ai/08-logic-and-reasoning.md) | Truth tables; modus ponens and tollens; invalid patterns | 4 | Drafted V2.0 |
| 09 | [Knowledge Representation](symbolic-ai/09-knowledge-representation.md) | Semantic network with inheritance; frames | 4 | Drafted V2.0 |
| 10 | [Rule-Based and Expert Systems](symbolic-ai/10-rule-based-and-expert-systems.md) | Laptop diagnosis with forward and backward chaining | 5 | Drafted V2.0 (pilot) |
| 11 | [Planning and Search](symbolic-ai/11-planning-and-search.md) | BFS vs DFS on a small map; preconditions and effects | 5 | Drafted V2.0 |
| 12 | [Symbolic NLP](symbolic-ai/12-symbolic-nlp.md) | Parsing "The cat sat"; keyword chatbot failures | 4, 6 | Drafted V2.0 |
| 13 | [Hands-on and Review](symbolic-ai/13-hands-on-and-review.md) | Six-rule study-method advisor; module review quiz | 5, 6 | Drafted V2.0 |

**How the topics connect.** Topics 01–06 build from "what is software" (01) through "how programs are written, built and store data" (02–04) to "how programs search, sort and organise data" (05–06). Topics 07–13 build from "what is Symbolic AI" (07) to logic (08), how knowledge is stored (09), how rules reason (10) and how search finds plans (11), then apply rules to language (12) and bring everything together (13). Key links: lists and binary search (05) need sorted arrays (06); the call stack in recursion (05) is a stack (06); queues and stacks (06) are the frontiers of BFS and DFS (11); trees (06) reappear as decision trees (07) and parse trees (12); logic programming (02) and declarative SQL (04) preview rules (08, 10). Topic 10 is the centre of Chapter 4 because it combines facts, rules and search.

**Every topic file uses the same template:** Learning Objectives · Explanation (with key terms) · Worked Example · Activity · Answer · Common Misunderstandings · Quick Self-Check · How This Topic Will Be Reused · References.

## Gaps and Uncertainties

- All 13 topics are drafted, but **none is "Checked" yet**: second-member reviews and beginner tests must be recorded in the Stage 2 logs (tasks T16, T22).
- Exact depth expected for Chapters 3 and 4 still needs confirming with the teacher (T9). Topics 03, 12 and 13 are kept brief as planned.
- Page or section numbers for textbook references still need confirming by the team.
- Optional extensions not covered (clearly outside the core scope): Big O notation beyond an intuitive mention, SQL JOIN syntax, merge sort and quicksort, heuristic search (A*), probabilistic reasoning.
