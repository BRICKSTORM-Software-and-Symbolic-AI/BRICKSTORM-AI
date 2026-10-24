# 05 Algorithms

**Chapter:** Chapter 3: Software & Algorithms  
**Status:** Drafted for searching only (V1.0). Sorting and recursion are outline only. Waiting for second-member review.  
**Proposed owner:** To be assigned (task T10)  
**Prerequisites:** Topic 06 helps (what a list is), but a list is explained here in one line.  
**Draft note:** Prepared with Claude assistance (AI-use record AI-4). The traces below were run with a short program.

## Learning Objectives

1. Define **algorithm** and explain why steps must be exact.
2. Carry out **linear search** and **binary search** by hand.
3. Explain why binary search needs a **sorted** list and why it is usually faster.
4. (Outline only) Describe a simple sort and recursion.

## Explanation

An **algorithm** is a finite list of exact steps that solves a problem. A recipe is similar, but an algorithm must be clear enough that a computer could follow it with no guessing.

A **list** is an ordered collection of items; each position has a number called an **index**, starting at 0.

**Searching** means finding where a target value is in a list (or finding that it is not there).

- **Linear search:** check items one by one from the start until you find the target or reach the end.
- **Binary search:** works only on a **sorted** list. Look at the middle item. If it equals the target, stop. If the target is bigger, discard the left half; if smaller, discard the right half. Repeat on the half that is left. Each step halves the search area.

Keep two markers, **low** and **high**, for the part still being searched, and compute **mid** = (low + high) // 2 (round down). Stop with "not found" when low > high.

```python
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid          # found: return the index
        elif items[mid] < target:
            low = mid + 1       # search the right half
        else:
            high = mid - 1      # search the left half
    return -1                   # not found
```

## Worked Example

List (sorted): `[3, 8, 12, 19, 25, 31, 40, 47]` with indexes 0 to 7. **Target: 31.**

| Step | low | high | mid | items[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 7 | 3 | 19 | 19 < 31, so discard the left half: low = 4 |
| 2 | 4 | 7 | 5 | 31 | Found at index 5 |

Binary search needed **2 checks**. Linear search would check 3, 8, 12, 19, 25, 31, which is **6 checks**.

## Activity

Using the same list:

1. Use binary search for **8**. Fill in a table like the one above. How many checks?
2. Use binary search for **10**. What happens, and how many checks before you can say "not found"?
3. Why would binary search give wrong results on `[12, 3, 47, 8]`?

## Answer

1. Step 1: low 0, high 7, mid 3, value 19 > 8, so high = 2. Step 2: low 0, high 2, mid 1, value 8. Found at index 1 after **2 checks**.
2. Step 1: mid 3 (19) > 10, high = 2. Step 2: low 0, high 2, mid 1 (8) < 10, low = 2. Step 3: low 2, high 2, mid 2 (12) > 10, high = 1. Now low (2) > high (1), so **not found after 3 checks**.
3. The method assumes that everything left of the middle is smaller and everything right is bigger. In an unsorted list that is false, so discarding half the list can throw away the target.

## Still to develop

Simple sorting (selection or bubble sort), recursion with one tracing example, and an intuitive comparison of speed for large lists.

## References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. (Binary search and algorithm basics.)
2. Foundations of CS & AI 2026, Chapter 3 course slides.

*The list and targets are the team's own example.*
