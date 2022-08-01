"""
Basic example to illustrate the result of the Branch and Bound algorithm
with the different heuristics implemented for a simple path problem of 
the Romania graph.

Expected Output:
----------------
[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
"""

# Search methods
import search

# Romania path problem
ab = search.GPSProblem('A', 'B', search.romania)

print("\n··· Resulting path by applying Branch and Bound algorithm using path cost as heuristic ···\n")

print("The path between A and B nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(ab).path()) + "]\n")

print("\n··· Resulting path by applying Branch and Bound algorithm using underestimation as heuristic ···\n")

print("The path between A and B nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(ab).path()) + "]\n")