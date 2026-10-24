
![Team logo](assets/team-logo.png)

# Brickstorm: Stage 1 Project Plan

**By:** Rawa Rashid, Batbaatar Undrakhjargal, Ochirsukh Bilguun, Myagmarsuren Batbileg, Turmunkh Binderya, Alsheryani Alia

October 20th–24th 2026

Foundations of CS & AI 2026 · Selected module: Software and Symbolic AI · Submission deadline: 24 October 2026, 23:59 (Beijing time)

**GitHub repository:** [paste the repository link here]

**Task list location:** snapshot in Section 6 below; live version in [tasks.md](tasks.md) in the repository.

## 1. Team Information and Responsibilities

**Team name:** Brickstorm  
**Selected module:** Software and Symbolic AI (Chapter 3: Software & Algorithms; Chapter 4: Symbolic AI)

| Member (as on class roster) | Role and responsibilities | Relevant strengths and experience | Skills to develop |
|---|---|---|---|
| Rawa Rashid | Content lead: keeps explanations accurate and consistent; develops the pilot topic; leads the Study Guide | Strong research, analytical thinking, academic writing, and ability to explain complex concepts clearly | Technical writing, content organization, and creating engaging educational materials |
| Batbaatar Undrakhjargal | Submission and logs: project log, personal-log reminders, AI-use records, test bank | Organized, detail-oriented, reliable in maintaining records and tracking progress | Documentation, time management, and developing effective assessment questions |
| Ochirsukh Bilguun | Coordinator: meetings, deadlines, task assignment, peer review, teacher contact | Communication, teamwork, organization, and problem-solving | Leadership, project management, conflict resolution, and delegation |
| Myagmarsuren Batbileg | Repository and submission lead: GitHub setup, branch and pull-request rules, final submissions | Technical problem-solving, logical thinking, and familiarity with digital tools | GitHub collaboration, version control, repository management, and troubleshooting |
| Turmunkh Binderya | Video lead: tutorial scripts, recording, editing | Creativity, communication, storytelling, and attention to detail | Video editing, recording techniques, scriptwriting, and educational video production |
| Alsheryani Alia | Visual design lead: slides, diagrams, visual consistency | Creativity, visual communication, attention to detail, and presentation skills | Graphic design, diagram creation, slide design, and visual |

**How we use strengths and share the workload.** Each member leads the area that matches their role and strengths, and also owns two or three topic files, so content work is spread evenly. Roles describe responsibility, not exclusive areas: every member studies the whole module, writes content, reviews another member's topic, and must be able to explain the team's core content. Each topic is checked by someone other than its author. The coordinator checks the task list every week and moves work from overloaded members to others.

## 2. Project Scope and Learning Goals

**Target learners.** First-time learners of computer science and AI, including students from non-technical majors. We assume basic computer use (files, browsers, apps) and no programming, logic, or mathematics beyond secondary school.

**Learning goals.** After using our materials, a beginner should be able to:

1. Explain the difference between system software and application software, and what an operating system does.
2. Describe how programming languages, software engineering practice, and databases support software development.
3. Trace simple algorithms (searching, sorting, recursion) by hand and explain basic data structures.
4. Explain what Symbolic AI is and how it represents knowledge with logic, facts, and rules.
5. Show how a rule-based system and a search procedure reach a conclusion, step by step.
6. Discuss real-world uses, strengths, and limits of Symbolic AI.

**Content outline.** Topic files are numbered 01–13. Depth: **D** = detailed (worked example, activity, answer); **B** = brief introduction.

| #  | Topic                         | Main subtopics                                                                                                        | Depth |
|-----|-------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------|
| 01  | Software Overview and OS      | System vs application software; functions of an OS (processes, memory, files, devices); common operating systems      | D     |
| 02  | Programming Languages         | Machine, assembly, and high-level languages; compiled vs interpreted; basic constructs (variables, conditions, loops) | D     |
| 03  | Software Engineering          | Development life cycle; requirements, design, testing, maintenance; version control                                   | B     |
| 04  | Databases and SQL             | Tables, keys, and relationships; basic SQL queries (SELECT, WHERE)                                                    | D     |
| 05  | Algorithms                    | What an algorithm is; linear and binary search; simple sorting; recursion; efficiency at an intuitive level           | D     |
| 06  | Data Structures               | Arrays, lists, stacks, queues, trees; choosing a structure for a task                                                 | D     |
| 07  | Intro to Symbolic AI          | History and idea of symbolic AI; symbols vs data-driven AI                                                            | D     |
| 08  | Logic and Reasoning           | Propositions, AND/OR/NOT, if-then; simple inference                                                                   | D     |
| 09  | Knowledge Representation      | Facts, rules, semantic networks, frames                                                                               | D     |
| 10  | Rule-Based and Expert Systems | Knowledge base and inference engine; forward and backward chaining; example expert system                             | D     |
| 11  | Planning and Search           | States and goals; breadth-first and depth-first search; planning problems                                             | D     |
| 12  | Symbolic NLP                  | Grammar rules, parsing, rule-based chatbots                                                                           | B     |
| 13  | Hands-on and Review           | Applications, advantages and limits of symbolic AI; review activities                                                 | B     |

**Scope boundaries.** Detailed treatment goes to ideas that beginners must understand to follow later topics: what an OS does, how a program is executed, how search and sorting work, and how rules produce conclusions.

Brief treatment goes to specialised material: software-engineering methodologies, advanced SQL, algorithmic complexity notation, formal logic proofs, and NLP. We will not teach full programming courses or machine learning.

**Points to confirm with the teacher.** (1) The exact expected coverage of Chapters 3 and 4 and the right level of difficulty. (2) The topic menu for the live mini lecture. (3) Whether the shared Markdown should keep Software and Symbolic AI in two separate folders (we currently do, as the teacher said verbally).

## 3. Planned Learning Resources and Mini Lecture

**Shared Markdown content.** The Markdown files in `content/` are the single source for all three resources. Each topic file uses the same template: Learning Objectives, Explanation, Worked Example, Activity, Answer, References. Images and diagrams live in `assets/` and are linked with relative paths. A topic is "ready for production" only after a second member has checked it.

**Study Guide and Test Bank.** The guide follows the topic order 01–13. Each chapter opens with its objectives, then explanation, a worked example, a short practice activity with answers, and a summary. The test bank contains multiple-choice and short-answer questions per topic, each tagged with a learning goal and with an answer explanation, so learners can practise and check understanding.

**PPT Slides.** One short deck per chapter section, built from the same objectives and examples. Slides use diagrams and step-by-step visuals: OS layers, a flowchart of how a program runs, a search tree for breadth-first vs depth-first search, and a rule-firing diagram for an expert system. Each slide carries one idea.

**Video Tutorials.** Short narrated tutorials for ideas that need demonstration:

1. What an operating system does
2. Binary search by hand
3. How a rule-based expert system reaches a conclusion
4. Search through a state space

Scripts come from the Markdown worked examples.

**Live Mini Lecture (proposed).** *How does a rule-based system reach a conclusion?*

It is a central Symbolic AI idea and can be taught in a few minutes. Audience activity: the class acts as the inference engine, applying printed if-then rules to given facts for a small diagnosis example, then compares forward and backward chaining. We will check this against the official topic menu and change it if needed.

**How the resources support one another.** The Markdown holds the explanation and the example. The Study Guide expands it for self-study, the slides turn it into visuals for teaching, and the videos demonstrate the processes. The test bank checks the same learning goals, and the mini lecture previews one example from the module. Any correction is made in Markdown first, then carried into the other deliverables.

## 4. Workflow, Schedule, and Coordination

**Studying the content.** Each member first studies the course slides for the whole module, then researches their own topics using the course materials and reliable references. Each topic owner writes a short summary for the team so everyone understands the core ideas.

**Developing and checking Markdown.** One pilot topic (proposed: 10 Rule-Based and Expert Systems) is developed completely first and used to test the template. After it passes review, the other topics follow the same pattern. Each draft goes through:

1. Author draft
2. Accuracy check by a second member
3. Beginner-readability check by a member from a non-technical background
4. Approval by the content lead before production begins

**Using GitHub.** The repository is created locally in VS Code, then published to GitHub. After the setup commit, nobody commits directly to `main`: each person works on a branch named after the task, opens a pull request, and another member reviews and merges it. Commit history and pull requests serve as contribution evidence. Tasks are tracked in `tasks.md`.

**Communication and meetings.** Daily messages on WeChat; in-person meetings in the dormitory at least twice a week (more near deadlines); a short checkpoint at each meeting to update task statuses. The coordinator records decisions in the project log.

**Getting corrections to every deliverable.** Errors are fixed in the Markdown first. The content lead then checks which of the Study Guide, test bank, slides, and videos are affected and assigns the owners to update them. A correction is closed only after all affected deliverables are updated.

**Testing and feedback.** Activities are tested on at least two outside beginners before Stage 2. The mini lecture is rehearsed at least twice, with timing and feedback each time. Peer feedback is collected after the Stage 2 first versions and applied in Stage 3.

**Schedule.**

| Stage                                     | Deadline    | Team internal checkpoints                                                                                                              |
|-------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Stage 1: Planning and content foundation  | 24 Oct 2026 | Repository rebuilt and published (24 Oct); all members review plan (24 Oct); pilot topic drafted (28 Oct) and checked (30 Oct)         |
| Stage 2: First versions and live teaching | 7 Nov 2026  | Topic drafts (2 Nov); cross-checks (4 Nov); guide, slides, test bank first versions (5 Nov); videos and mini lecture rehearsed (6 Nov) |
| Stage 3: Review, revision, final delivery | 28 Nov 2026 | Feedback round (14 Nov); revisions in all deliverables (21 Nov); final production (25 Nov); final package check (27 Nov)               |

**Main risks and responses.**

| Risk                                      | Response                                                                                           |
|-------------------------------------------|----------------------------------------------------------------------------------------------------|
| Unfamiliar tools (Git, VS Code, Markdown) | Admin helps others clone and make their first branch; short practice session in the first week     |
| Difficult content (logic, search, SQL)    | Pair a technical and a non-technical member on hard topics; ask the teacher early                  |
| Uneven workload                           | Weekly check of the task list; coordinator reassigns tasks                                         |
| Delayed tasks                             | Internal deadlines at least one day before real ones; blocked tasks are raised at the next meeting |
| Deliverables out of sync                  | Markdown is the single source; correction procedure above                                          |
| Repository or upload problems             | Keep a local ZIP copy of every milestone                                                           |

## 5. Records, Contributions, and AI Use

The team keeps a project log and each member keeps a personal log. Planning discussions on 20 and 22 October and the teacher instructions of 23 October are recorded in the project log. AI assistance (Claude) was used for turning slides into study material, paraphrasing member strengths, and building and restructuring the repository. Each use is recorded in the AI-use log under Section 6 of the Shared Assignment Rules, with what the team checked and changed. The team has reviewed this plan and can explain and justify it.

## 6. Master Task List (snapshot, 24 October 2026)

Status: Not started / In progress / Under review / Completed. Stage 1 tasks are detailed; Stage 2 and 3 tasks will be refined.

| ID  | Task                                                                                                                                              | Expected result                                                  | Responsible (lead first)              | Internal deadline | Status      | Depends on         |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------|-------------------|-------------|--------------------|
| T1  | Rebuild the repository in VS Code following the student guide and publish it to GitHub                                                            | Published repository with README.md, tasks.md, content/, assets/ | Myagmarsuren, Rawa                    | 24 Oct            | In progress | None               |
| T2  | Invite all members and confirm each can clone the repository                                                                                      | Six members with access; each has the local copy                 | Myagmarsuren                          | 24 Oct            | Not started | T1                 |
| T3  | Finalize the project plan and task list                                                                                                           | Final plan document                                              | Ochirsukh, Turmunkh, Batbaatar        | 24 Oct            | In progress | None               |
| T4  | All members review and approve the plan                                                                                                           | Review confirmed in the project log                              | All; Ochirsukh leads                  | 24 Oct            | Not started | T3                 |
| T5  | Submit Brickstorm_Stage1_ProjectPlan with the repository link                                                                                     | One submission by the submission lead                            | Myagmarsuren (backup: Batbaatar)      | 24 Oct            | Not started | T1, T4             |
| T6  | Update the project log and start personal logs                                                                                                    | Project log current; six personal logs started                   | Batbaatar                             | 24 Oct            | In progress | None               |
| T7  | Write the AI-use records (AI-1 to AI-3) with what was checked and changed                                                                         | Complete entries in the log                                      | Batbaatar, each member                | 24 Oct            | In progress | None               |
| T8  | Prepare visual style and first assets                                                                                                             | Palette, fonts, one diagram in assets/                           | Alia                                  | 24 Oct            | In progress | None               |
| T9  | Confirm scope, difficulty, and the mini lecture topic menu with the teacher                                                                       | Written notes of the teacher's answers                           | Ochirsukh                             | 26 Oct            | Not started | T3                 |
| T10 | Assign topic owners and reviewers for topics 01–13                                                                                                | Owner and reviewer filled in each topic file and in tasks.md     | Ochirsukh                             | 27 Oct            | Not started | T2                 |
| T11 | Develop the pilot topic fully (proposed: 10 Rule-Based and Expert Systems): objectives, explanation, worked example, activity, answer, references | Completed topic file in content/symbolic-ai/                     | Rawa                                  | 28 Oct            | Not started | T2, T10            |
| T12 | Verify the pilot topic for accuracy and beginner readability                                                                                      | Review comments resolved                                         | Turmunkh, Ochirsukh                   | 30 Oct            | Not started | T11                |
| T13 | Peer review record for the pilot topic                                                                                                            | Record in the log or repository                                  | Ochirsukh                             | 1 Nov             | Not started | T12                |
| T14 | Draft topics 01–06 (Software and Algorithms)                                                                                                      | Six checked topic files                                          | Topic owners; Rawa checks consistency | 2 Nov             | Not started | T12                |
| T15 | Draft topics 07–13 (Symbolic AI)                                                                                                                  | Seven checked topic files                                        | Topic owners; Rawa checks consistency | 2 Nov             | Not started | T12                |
| T16 | Cross-check each topic by a second member                                                                                                         | Review comments resolved in pull requests                        | All                                   | 4 Nov             | Not started | T14, T15           |
| T17 | Study Guide first version                                                                                                                         | Guide compiled from the Markdown                                 | Rawa, Batbaatar                       | 5 Nov             | Not started | T16                |
| T18 | Test bank first version                                                                                                                           | At least five tagged questions with explanations per topic       | Batbaatar, topic owners               | 5 Nov             | Not started | T16                |
| T19 | PPT Slides first version with diagrams                                                                                                            | First deck per chapter                                           | Alia, topic owners                    | 5 Nov             | Not started | T16                |
| T20 | Video scripts and first recordings                                                                                                                | Scripts and 1–2 recorded tutorials                               | Turmunkh                              | 6 Nov             | Not started | T16                |
| T21 | Prepare and rehearse the mini lecture                                                                                                             | Script, activity materials, two timed rehearsals                 | Ochirsukh, Rawa                       | 5 Nov             | Not started | T9                 |
| T22 | Test activities on outside beginners                                                                                                              | Feedback notes and changes made                                  | Ochirsukh                             | 5 Nov             | Not started | T16                |
| T23 | Stage 2 submission check                                                                                                                          | Complete package ready                                           | Myagmarsuren                          | 6 Nov             | Not started | T17–T21            |
| T24 | Feedback and peer review round                                                                                                                    | Feedback list with decisions                                     | All; Ochirsukh leads                  | 14 Nov            | Not started | Stage 2 submission |
| T25 | Revise Markdown and update all affected deliverables                                                                                              | Updated Markdown, guide, test bank, slides, videos               | Topic owners; Rawa checks             | 21 Nov            | Not started | T24                |
| T26 | Final production of guide, slides, videos                                                                                                         | Final versions                                                   | Rawa, Alia, Turmunkh                  | 25 Nov            | Not started | T25                |
| T27 | Final logs, AI-use records, contribution evidence, and ZIP package                                                                                | Final package                                                    | Batbaatar, Myagmarsuren               | 27 Nov            | Not started | T26                |
