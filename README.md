# Homework 1: Graph ADT & Traversals

Follow the instructions [here](https://make-school-courses.github.io/CS-2.2-Graphs-Recursion/#/Assignments/01-Graph-ADT) to complete this assignment.

## Discussion Questions

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

When doing BFS on a graph it is different because a graph could contain cycles (this means some vertices could be re-visited if not taken note of), while a tree is straightforward layer by layer without worrying about cycles. Also graphs could be either undirected or directed, meaning its edges could have a set and stone path (if directed) or no direction at all (if undirected). We can also start bfs from anywhere on the graph where in trees we start at the root node.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

BFS could be used whenever traveling and using a GPS. The computer finds all possible paths using BFS and then displays to us the shortest/fastest path.
