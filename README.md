# README
Solutions created for the problem set proposed by Huron Digital Pathology.

## Problem set

### problem 1
Given the following set of numbers S={49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46}.
A function picks a random subset of size 6, and returns the minimum of that subset.
What is the expected value of this function?
Please solve it by 2 ways: a) Analytical solution b) Programmatically, both in C++ and Python

### problem 2
I want you to read paper titled “Yottixel – An Image Search Engine for Large Archives of Histopathology Whole Slide Images” which can be found at: https://www.sciencedirect.com/science/article/pii/S1361841520301213

I want you to write an paragraph or 2 on how you would improve “Algorithm 2. Distance between two given WSIs I_q and I” in the paper for better search accuracy. Please note that there is no right or wrong answer to this question.

Please let me know if you have problems accessing the paper.

## Approach
Given the context, I tried to solve this problem set without asking any obvious questions and, at the same time, showing independency. Although, some questions did arise, for instance:
- Are tests for the first solution optional?
- Should I focus on improving complexity (time or space?) or just best practices for software development?
- The first problem is very constrained, should I generalize it or stick to the original problem?
- show performance and deployment in the project's documentation?

#Development

## Platform
Source code of the project can be found at [https://github.com/guidotorresmx/problem-set-huron](github), which could become private or deleted in the future.


## Links to solutions
- [Analytical and Programmatical solution in c++ ->   ](solution-to-problem-1/cpp)
- [Analytical and Programmatical solution in python ->](solution-to-problem-1/python)

## Sample results

each number can be the minimum of the subset, exactly the following percent of
the times for the set: S={49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46} and
sampling size of 6

```
     4 = 46.15%
     8 = 26.92%
    15 = 14.69%
    16 = 07.34%
    23 = 03.26%
    42 = 01.22%
    43 = 00.35%
    44 = 00.06%
    45 = 00.00%
    46 = 00.00%
    47 = 00.00%
    48 = 00.00%
    49 = 00.00%
```