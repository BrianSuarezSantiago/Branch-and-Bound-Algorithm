<a href="https://numpy.org">
    <img align="right" src="https://custom-icon-badges.herokuapp.com/badge/NumPy-14354C.svg?logo=numpylogo" alt="NumPy">
</a>

<a href="https://www.python.org">
    <img align="right" src="https://custom-icon-badges.herokuapp.com/badge/Python-14354C.svg?logo=pythonlogo" alt="Python">
</a>

<h1 align="center">💠 Branch and Bound Algorithm 🏵</h1>


<p align="center">
    <img src="./assets/Algorithm Execution.gif" alt="Branch and Bound Algorithm Execution">
    <sub>· Execution of Branch and Bound Algorithm ·</sub>
</p>


## 📚 Fundamentals

- ***Branch and Bound Algorithm***

The Branch and Bound search strategy belong to the uninformed search strategies. Its operating principle is based on sorting the open list using as a criterion the cumulative cost of each partial path, represented by each node of the open list. Therefore, the first node of the list will be expanding and generating new trajectories by the ramification of its children.

- ***Branch and Bound Underestimation Algorithm***

The branch and bound search strategy with underestimation belong to the informed search strategies. In this case, in addition to using the cumulative cost of a path from the initial state to a certain state of the network, a heuristic estimate to the final state is used to sort the open list. Thus, given a given node n in the search tree, the estimated cost expression f(n) will be:

`f(n) = g(n) + h(n)`

Where g(n) represents the accumulated cost and h(n) the heuristic used. For the path found to be optimal, the heuristic must be consistent. That is, it must fulfill that for each node n and each child node n' reached using action a, the heuristic value h(n) must always be less or equal to the heuristic value h(n') plus the cost from node n to n' through action a.

`h(n) ≤ c(n, a, n') + h(n')`

<img src="./assets/Romania Graph.png" alt="Romania Graph" width="500px" heigth="200px">


## 👨🏻‍💻 Implementation

The development of this practice consists of two parts. The first consists of the development of an uninformed search algorithm called Branch and Bound.

In essence, the most significant change in the implementation of this algorithm concerning a FIFO queue or a Stack is that before expanding each of the nodes, it orders them according to their cost. The sorting is done through the lambda function named node which takes into account the path_cost of each node.

On the other hand, the second version of the Branch and Bound algorithm is based on the use of the BranchBoundUnderstimation class, which orders each of the nodes according to the path cost plus the heuristic cost.


## 📈 Visualization of generated and visited nodes

Below is a comparative table of the expanded and visited nodes for each of the paths according to the search algorithm used for the Romania graph.

*Expanded Nodes*

| Paths Problems | Breadth First Search | Depth First Search | Branch and Bound | Branch and Bound with Underestimation |
| :---: | :---:| :---:| :---:| :---:|
| A → B |  8   |  7   |  12  |  5   |
| F → P |  7   |  3   |  6   |  3   |
| A → U |  12  |  14  |  13  |  8   |
| D → I |  17  |  18  |  18  |  12  |
| H → R |  10  |  6   |  8   |  4   |

*Visited Nodes*

| Paths Problems | Breadth First Search | Depth First Search | Branch and Bound | Branch and Bound with Underestimation |
| :---: | :---:| :---:| :---:| :---:|
| A → B |  16  |  10  |  24  |  6   |
| F → P |  9   |  6   |  9   |  4   |
| A → U |  22  |  28  |  30  |  9   |
| D → I |  40  |  40  |  42  |  19  |
| H → R |  16  |  10  |  13  |  5   |


## 💾 Expected Outputs

The results of running each of the search algorithms for each of the path can be found [here.](./docs/)


## 🚀 Build the project

1. Clone the repository using git with `git clone https://github.com/BrianSuarezSantiago/Branch-and-Bound-Algorithm.git` command or download from [Source Code.](https://github.com/BrianSuarezSantiago/Branch-and-Bound-Algorithm/archive/refs/heads/master.zip)

2. Move to the directory where you have the code.

3. Compile and execute the source code using the `python3 run.py` command.

<hr>
<p align="center">
Made with ♥️ in Spain
</p>
