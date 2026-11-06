# Stage 2 Notes (V2.0, 3 November 2026)

Working notes for the Stage 2 submission report. The report should stay concise; copy the tables below and add the team's own review evidence, commit identifiers and teacher feedback.

## 1. Revision Summary

No written teacher feedback on Stage 1 was available in the repository when V2.0 was drafted, so the revisions below come from the team's own review against the Stage 1 gaps list, the Stage 2 brief and the Chapter 3 course slides. **Add any teacher or status-report feedback as new rows.**

| Feedback or problem | What changed and why | Where to find the change |
|---|---|---|
| Nine of 13 topics were outline only (Stage 1 gaps list) | Wrote full learning content for every topic: explanation, key terms, worked example, activity, checked answers, references | `01`–`04`, `06`, `07`, `11`, `12`, `13`: all sections |
| Topic 05 covered searching only; sorting and recursion missing | Added algorithm features, three ways of writing an algorithm (with a flowchart), bubble and selection sort, iteration vs recursion with a call trace, and an intuitive efficiency table | `05-algorithms.md`: "Three ways to write an algorithm", "Sorting", "Iteration and recursion", "Efficiency", Worked Examples 2–3 |
| Coverage did not match all items on the Chapter 3 course slides | Added OS evolution and process/memory management (01), language evolution and categories (02), process models, modularity and QA (03), database models (04), records, linked lists, binary trees and graphs (06) | Explanation sections of `01`–`04`, `06` |
| Activities in V1.0 were mostly recall or single tracing tasks | Every topic now mixes tracing, predicting, find-the-error, comparing and explaining-a-decision tasks | "Activity" in every topic file |
| Beginners' likely confusions were not addressed | Added a "Common Misunderstandings" section to all 13 topics (e.g. `=` vs `==`, WHERE vs SELECT, OR is inclusive, parsing ≠ understanding) | "Common Misunderstandings" in every topic file |
| Topic 08 taught only one valid and one invalid pattern; rules with variables used in 09–10 were never introduced | Added modus tollens, denying the antecedent, a four-patterns table and rules with variables | `08-logic-and-reasoning.md`: "Explanation", "Rules with variables", Activity 4–5 |
| Topic 09 named frames but gave no worked example; "not stored" vs "false" was unclear | Added a frame worked example with inheritance and override, a comparison table and the closed-world note | `09-knowledge-representation.md`: "Comparing the four forms", "Worked example with frames" |
| Topic 10 did not say what happens when several rules can fire, or link to logic and search | Added conflict resolution and explicit links to modus ponens (08) and search (11) | `10-rule-based-and-expert-systems.md`: "When more than one rule can fire" |
| Hand traces could contain arithmetic slips | Every computable example and answer is re-run by `tools/check_examples.py`; output matched all hand traces | `tools/check_examples.py` |
| Only three diagrams existed | Added 13 diagrams in the same colour style | `assets/diagrams/`, listed in `assets/README.md` |
| Status labels in README and outline were out of date | Updated status tables, version history and gaps | `README.md`, `content/00-module-outline.md`, `tasks.md` |

**Suggestions not adopted:** Big O notation, SQL JOIN syntax and heuristic search (A*) are mentioned only briefly and labelled optional, because the project plan limits algorithmic complexity and advanced SQL to brief treatment for beginners.

## 2. Accuracy and Usability Checks

**Done so far (automated):** `python tools/check_examples.py` reproduces the round-robin traces (01), program outputs (02), all SQL results (04), binary search, sorting and recursion traces (05), stack, queue and BST traces (06), truth tables (08), forward-chaining runs (10, 13), BFS/DFS orders and paths (11) and chatbot replies (12). All matched the Markdown on 3 Nov 2026.

**Still to do and record in the Stage 2 logs (beside the relevant entries):**

| Topic | Author | Second-member reviewer | Beginner tester (activity) | What they understood / where confused / what changed |
|---|---|---|---|---|
| 01 | | | | |
| 02 | | | | |
| 03 | | | | |
| 04 | | | | |
| 05 | | | | |
| 06 | | | | |
| 07 | | | | |
| 08 | | | | |
| 09 | | | | |
| 10 | Rawa | | | |
| 11 | | | | |
| 12 | | | | |
| 13 | | | | |

Reviewer checklist: claims agree with the references; examples and answers correct (run `tools/check_examples.py`); activity can be done with only the information given; terms consistent with other topics; references exist; images display in the extracted ZIP.

## 3. Resource Mapping (draft)

| Markdown topic / section | Study Guide / Test Bank use | PPT use | Video Tutorial use |
|---|---|---|---|
| `01` Explanation, Worked Examples 1–2 | Ch. 1; Qs on sorting software, OS jobs, round-robin trace | Layers figure; OS-jobs table; double-click steps; round-robin table | Tutorial 1 "What an operating system does" |
| `02` Worked Example, Activity | Ch. 2; predict-the-output, find-the-error | Language levels; compiler vs interpreter; trace table | Not selected for video |
| `03` Worked Example, Activity 1 | Ch. 3 (short); "which stage?" Qs | SDLC table; waterfall vs agile figure | Not selected for video |
| `04` Worked Example, Activity 1 | Ch. 4; predict-the-rows Qs | Linked tables figure; four-step query method | Not selected for video |
| `05` Worked Examples 1–3, Activity 1–6 | Ch. 5; tracing Qs for search, sort, recursion | Flowchart; binary search table; bubble sort passes | Tutorial 2 "Binary search by hand" |
| `06` Worked Example, Activity 1–5 | Ch. 6; stack/queue/BST traces, choose-a-structure | Structures table; stack/queue, linked list, BST figures | Not selected for video (Back-button clip optional) |
| `07` Worked Example, Activity 3 | Ch. 7; S/D/M classification, timeline | Symbolic vs data-driven table; decision tree | Not selected (opening of Tutorial 3 optional) |
| `08` Truth table, four patterns | Ch. 8; truth-table and valid/invalid Qs | Truth table; patterns table | Inside Tutorial 3 (modus ponens = firing a rule) |
| `09` Worked examples, Figure 1 | Ch. 9; inheritance and frame Qs | Semantic network; frames | Not selected for video |
| `10` Worked Example (forward and backward) | Ch. 10; chaining Qs | Architecture figure; rule-chain figure; forward table | Tutorial 3 "How a rule-based expert system reaches a conclusion"; live mini lecture |
| `11` Worked Example, Activity 1–3 | Ch. 11; BFS/DFS trace Qs | Map; BFS queue table; search trees | Tutorial 4 "Search through a state space" |
| `12` Worked Example, chatbot | Ch. 12 (short); parsing and chatbot-failure Qs | Parse tree; canteen bot table | Not selected for video |
| `13` Worked Example, Part B quiz | Ch. 13; cumulative test-bank items | Build method; advisor chain; applications table | Not selected (advisor as Tutorial 3 extension) |

## 4. Remaining Gaps and Next Steps

- No topic is "Checked" until the reviews above are recorded (T16, T29).
- Topic owners and reviewers must be filled in `tasks.md` (T10).
- Textbook references list chapters/sections; page numbers still to be confirmed.
- Diagrams are functional drafts; the visual design lead may restyle them (keep file names so links still work).
- The test bank needs at least five tagged questions per topic (T18); the Activities, Self-Checks and Topic 13 quiz supply the first items.

## 5. AI Use (for the Stage 2 logs)

**AI-5 (3 Nov 2026), Claude:** drafted the nine outline-only topics from the team's existing outlines, extended Topic 05, revised Topics 08–10, produced 13 diagrams and the two scripts in `tools/`, and drafted these notes. Verification: all computable examples re-run by script. **Still required from the team:** each topic owner reads, checks against the references, edits, and records what they changed and learned beside this entry in the project and personal logs.
