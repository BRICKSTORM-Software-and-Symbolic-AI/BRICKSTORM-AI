# 08 Logic and Reasoning

**Chapter:** Chapter 4: Symbolic AI  
**Status:** Drafted (V2.0, 3 Nov 2026; V1.0 24 Oct). V2.0 adds modus tollens, variables in rules, misunderstandings, self-check and reuse notes. Truth tables checked by a short program. Waiting for second-member review (see `tasks.md`, T16).  
**Owner / reviewer:** see `tasks.md` (T10)  
**Prerequisites:** Topic 07 (what Symbolic AI is). No mathematics beyond everyday true/false thinking.  
**Draft note:** Prepared with Claude assistance (AI-use records AI-4 and AI-5); to be checked by a team member.

## Learning Objectives

1. Explain what a **proposition** is and combine propositions with AND, OR, NOT and IF-THEN.
2. Complete a truth table for a simple statement.
3. Use **modus ponens** and **modus tollens** to draw valid conclusions, and spot the two common invalid patterns.
4. Read a rule with a **variable** (X) and apply it to a specific case.

## Explanation

**Logic** is the study of correct reasoning. Symbolic AI uses logic so that a computer can reason with statements in a fixed, checkable way.

A **proposition** is a statement that is either true or false, for example "It is raining". Questions and commands are not propositions. We usually name propositions with letters, such as **P** = "It is raining" and **Q** = "The road is wet".

Propositions can be combined:

| Symbol | Name | Meaning | Example |
|---|---|---|---|
| P AND Q | Conjunction | True only if both are true | It is raining AND the road is wet |
| P OR Q | Disjunction | True if at least one is true | It is raining OR the sprinkler is on |
| NOT P | Negation | Flips true and false | It is NOT raining |
| IF P THEN Q | Implication | A rule: false only when P is true and Q is false | IF it is raining THEN the road is wet |

A **truth table** lists every possible combination of true (T) and false (F) and gives the result:

| P | Q | P AND Q | P OR Q | NOT P | IF P THEN Q |
|---|---|---|---|---|---|
| T | T | T | T | F | T |
| T | F | F | T | F | **F** |
| F | T | F | T | T | T |
| F | F | F | F | T | T |

Beginners often find the last two rows of IF-THEN odd. Think of it as a promise: "If it rains, the road is wet." The promise is broken only when it rains and the road is dry. If it is not raining, the promise says nothing, so it is not broken.

**Inference** means using known statements to reach a new one. The basic valid pattern is **modus ponens**: if "IF P THEN Q" is true and P is true, then Q must be true. This is exactly what a rule-based system does when it fires a rule (Topic 10).

A second valid pattern is **modus tollens**: if "IF P THEN Q" is true and Q is **false**, then P must be false. (If rain always makes the road wet, and the road is dry, it is not raining.)

Two common **invalid** patterns (they look convincing but do not follow):

| Pattern | Form | Why it fails |
|---|---|---|
| *Affirming the consequent* | IF P THEN Q; Q is true; so P is true | Something else may have made Q true |
| *Denying the antecedent* | IF P THEN Q; P is false; so Q is false | Q may be true for another reason |

| | Know | Conclude | Valid? |
|---|---|---|---|
| Modus ponens | IF P THEN Q, and P | Q | ✔ |
| Modus tollens | IF P THEN Q, and NOT Q | NOT P | ✔ |
| Affirming the consequent | IF P THEN Q, and Q | P | ✘ |
| Denying the antecedent | IF P THEN Q, and NOT P | NOT Q | ✘ |

### Rules with variables

So far each letter stood for one fixed statement. AI rules usually talk about **any** object, using a **variable** such as X: **IF X is a dog THEN X is a mammal**. To use the rule, we **substitute** a specific object for X: with the fact "Rex is a dog", X = Rex, so "Rex is a mammal" follows by modus ponens. This step from one-off statements to statements about "any X" is the idea behind **predicate logic** (also called first-order logic), which Topics 09 and 10 rely on.

## Worked Example

Statements: **Rule:** IF it is raining THEN the road is wet. **Fact:** It is raining.

1. Name the parts: P = "It is raining", Q = "The road is wet".
2. We know "IF P THEN Q" is true.
3. We know P is true.
4. By modus ponens, Q is true: **the road is wet**.

Now change the fact to "The road is wet". Can we conclude it is raining? No. A sprinkler or a cleaning truck could also wet the road, so Q being true does not force P to be true.

Now change the fact to "The road is **not** wet". By **modus tollens**, it is **not raining**. And if the fact is "It is **not** raining", we can conclude nothing about the road (denying the antecedent would be invalid).

## Activity

1. Rule: "IF a number is divisible by 4 THEN it is even". Fact: 12 is divisible by 4. What follows?
2. Rule: "IF the library is open THEN students can borrow books". Fact: students can borrow books. Can you conclude the library is open?
3. Complete the truth table for **P AND (NOT Q)**.

| P | Q | NOT Q | P AND (NOT Q) |
|---|---|---|---|
| T | T | | |
| T | F | | |
| F | T | | |
| F | F | | |

4. Rule: "IF X is a square THEN X has four sides". (a) Fact: shape K is a square. What follows, and what did X stand for? (b) Fact: shape M does **not** have four sides. What follows, and by which pattern? (c) Fact: shape T is **not** a square. Can you conclude that T does not have four sides?
5. **Find the error.** A student reasons: "IF a student studies THEN they pass. Bat did not study. So Bat failed." Name the mistake and give a situation that shows the conclusion could be wrong.

## Answer

1. 12 is even (modus ponens).
2. No. Books might be borrowed through another service, so this is the invalid pattern of affirming the consequent.
3. Rows: T,T → NOT Q = F, result **F**; T,F → T, **T**; F,T → F, **F**; F,F → T, **F**. Only P true and Q false makes the statement true.
4. (a) X = K, so **K has four sides** (modus ponens). (b) **M is not a square** (modus tollens). (c) **No.** A rectangle is not a square but still has four sides; this would be denying the antecedent.
5. **Denying the antecedent.** The rule only says what happens if a student studies; it says nothing about students who do not. Bat might already know the material, or the test might be easy, and still pass.

## Common Misunderstandings

- *"OR means one or the other, but not both."* In logic, P OR Q is also true when **both** are true (row 1 of the truth table).
- *"IF P THEN Q also means IF Q THEN P."* It does not; reversing a rule is exactly the error of affirming the consequent.
- *"A valid argument always has a true conclusion."* Validity is about the **form**: if the starting statements are true, the conclusion must be true. If a starting rule is false, a valid argument can still reach a false conclusion.

## Quick Self-Check

1. When is IF P THEN Q false? *(Only when P is true and Q is false.)*
2. From IF P THEN Q and NOT Q, what follows? *(NOT P, by modus tollens.)*
3. Is "Close the door!" a proposition? *(No; a command is neither true nor false.)*

## How This Topic Will Be Reused

- **Study Guide / Test Bank:** chapter "Logic and Reasoning"; truth-table completion, valid/invalid argument questions, rule-with-variable questions.
- **PPT Slides:** connectives table, truth table built row by row, the four-patterns table.
- **Video Tutorial:** not selected as a separate video; modus ponens is explained inside tutorial 3 (expert systems), where it is what "firing a rule" means.

## References

1. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. (Chapters on logical agents and first-order logic.)
2. Rosen, K. H. (2019). *Discrete Mathematics and Its Applications* (8th ed.). McGraw-Hill. (Propositions, truth tables, rules of inference and fallacies.)
3. Foundations of CS & AI 2026, Chapter 4 course slides.

*Example sentences are the team's own.*
