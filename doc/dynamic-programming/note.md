# Dynamic Programming

## Summary

- Optimal substructure
  - An optimal solution to a problem (instance) contains optimal solution to sub-problems.
- Overlapping sub-problems
  - A recursive solution contains a "small" number of distinct sub-problems repeated many times.

## Every Dynamic Programming problem has 4 steps:

- Show that the problem can be broken down into optimal sub-problems.
- Recursively define the value of the solution by expressing it in terms of optimal solutions for smaller sub-problems.
- Computer the value of the optimal solution in bottom-up fashion.
- Construct an optimal solution from the computed information.
