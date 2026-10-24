# 08 Logic and Reasoning

**Chapter:** Chapter 4: Symbolic AI  
**Status:** Drafted (V1.0). Waiting for second-member review.  
**Proposed owner:** To be assigned (task T10)  
**Prerequisites:** Topic 07 (what Symbolic AI is). No mathematics beyond everyday true/false thinking.  
**Draft note:** Prepared with Claude assistance (AI-use record AI-4); to be checked by a team member.

## Learning Objectives

1. Explain what a **proposition** is and combine propositions with AND, OR, NOT and IF-THEN.
2. Complete a truth table for a simple statement.
3. Use **modus ponens** to draw a valid conclusion, and spot an invalid one.

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

A common **invalid** pattern is *affirming the consequent*: from "IF P THEN Q" and Q, we cannot conclude P.

## Worked Example

Statements: **Rule:** IF it is raining THEN the road is wet. **Fact:** It is raining.

1. Name the parts: P = "It is raining", Q = "The road is wet".
2. We know "IF P THEN Q" is true.
3. We know P is true.
4. By modus ponens, Q is true: **the road is wet**.

Now change the fact to "The road is wet". Can we conclude it is raining? No. A sprinkler or a cleaning truck could also wet the road, so Q being true does not force P to be true.

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

## Answer

1. 12 is even (modus ponens).
2. No. Books might be borrowed through another service, so this is the invalid pattern of affirming the consequent.
3. Rows: T,T → NOT Q = F, result **F**; T,F → T, **T**; F,T → F, **F**; F,F → T, **F**. Only P true and Q false makes the statement true.

## References

1. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. (Chapters on logical agents.)
2. Foundations of CS & AI 2026, Chapter 4 course slides.

*Example sentences are the team's own.*
