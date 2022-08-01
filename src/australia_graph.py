# Search methods
import search

# Australia path problems
v_sa = search.GPSProblem('V', 'SA', search.australia)
wa_wa = search.GPSProblem('WA', 'WA', search.australia)
q_q = search.GPSProblem('Q', 'Q', search.australia)
sa_nsw = search.GPSProblem('SA', 'NSW', search.australia)
nt_nt = search.GPSProblem('NT', 'NT', search.australia)

print("··· Resulting paths by applying Breadth First Search algorithm ···\n")

print("The path between V and SA nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(v_sa).path()) + "]\n")
print("The path between WA and WA nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(wa_wa).path()) + "]\n")
print("The path between Q and Q nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(q_q).path()) + "]\n")
print("The path between SA and NSW nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(sa_nsw).path()) + "]\n")
print("The path between NT and NT nodes is [" + ', '.join(str(v) for v in search.breadth_first_graph_search(nt_nt).path()) + "]\n")


print("\n··· Resulting paths by applying Depth First Search algorithm ···\n")

print("The path between V and SA nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(v_sa).path()) + "]\n")
print("The path between WA and WA nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(wa_wa).path()) + "]\n")
print("The path between Q and Q nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(q_q).path()) + "]\n")
print("The path between SA and NSW nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(sa_nsw).path()) + "]\n")
print("The path between NT and NT nodes is [" + ', '.join(str(v) for v in search.depth_first_graph_search(nt_nt).path()) + "]\n")


print("\n··· Resulting paths by applying Branch and Bound algorithm using path cost as heuristic ···\n")

print("The path between V and SA nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(v_sa).path()) + "]\n")
print("The path between WA and WA nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(wa_wa).path()) + "]\n")
print("The path between Q and Q nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(q_q).path()) + "]\n")
print("The path between SA and NSW nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(sa_nsw).path()) + "]\n")
print("The path between NT and NT nodes is [" + ', '.join(str(v) for v in search.branch_and_bound(nt_nt).path()) + "]\n")


print("\n··· Resulting paths by applying Branch and Bound algorithm using underestimation as heurisitic ···\n")

print("The path between V and SA nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(v_sa).path()) + "]\n")
print("The path between WA and WA nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(wa_wa).path()) + "]\n")
print("The path between Q and Q nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(q_q).path()) + "]\n")
print("The path between SA and NSW nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(sa_nsw).path()) + "]\n")
print("The path between NT and NT nodes is [" + ', '.join(str(v) for v in search.branch_and_bound_with_underestimation(nt_nt).path()) + "]\n")