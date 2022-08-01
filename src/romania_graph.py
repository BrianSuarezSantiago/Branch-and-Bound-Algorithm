# Search methods
import search

# Romania path problems
ab = search.GPSProblem('A', 'B', search.romania)
fp = search.GPSProblem('F', 'P', search.romania)
au = search.GPSProblem('A', 'U', search.romania)
di = search.GPSProblem('D', 'I', search.romania)
hr = search.GPSProblem('H', 'R', search.romania)

print("··· Resulting paths by applying Breadth First Search algorithm ···\n")

print("The path between A and B nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(ab).path()) + "]\n")
print("The path between F and P nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(fp).path()) + "]\n")
print("The path between A and U nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(au).path()) + "]\n")
print("The path between D and I nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(di).path()) + "]\n")
print("The path between H and R nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(hr).path()) + "]\n")


print("\n··· Resulting paths by applying Depth First Search algorithm ···\n")

print("The path between A and B nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(ab).path()) + "]\n")
print("The path between F and P nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(fp).path()) + "]\n")
print("The path between A and U nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(au).path()) + "]\n")
print("The path between D and I nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(di).path()) + "]\n")
print("The path between H and R nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(hr).path()) + "]\n")


print("\n··· Resulting paths by applying Branch and Bound algorithm using path cost as heuristic ···\n")

print("The path between A and B nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(ab).path()) + "]\n")
print("The path between F and P nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(fp).path()) + "]\n")
print("The path between A and U nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(au).path()) + "]\n")
print("The path between D and I nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(di).path()) + "]\n")
print("The path between H and R nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(hr).path()) + "]\n")


print("\n··· Resulting paths by applying Branch and Bound algorithm using underestimation as heurisitic ···\n")

print("The path between A and B nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(ab).path()) + "]\n")
print("The path between F and P nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(fp).path()) + "]\n")
print("The path between A and U nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(au).path()) + "]\n")
print("The path between D and I nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(di).path()) + "]\n")
print("The path between H and R nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(hr).path()) + "]\n")