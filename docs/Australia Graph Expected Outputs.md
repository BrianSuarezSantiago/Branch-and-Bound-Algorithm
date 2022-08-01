#  Expected outputs for differents search methods


## 🔸 Breadth First Search Algorithm

  <ins>
  First Case:
  </ins>
  
    Initial Node: V
    Goal Node: SA
    Path: [<Node SA>, <Node V>]
    Cost: 1

  <ins>
  Second case:
  </ins>

    Initial Node: WA
    Goal Node: WA
    Path: [<Node WA>]
    Cost: 0

  <ins>
  Third case:
  </ins>

    Initial Node: Q
    Goal Node: Q
    Path: [<Node Q>]
    Cost: 0

  <ins>
  Fourth Case:
  </ins>

    Initial Node: SA
    Goal Node: NSW
    Path: [<Node NSW>, <Node SA>]
    Cost: 1

  <ins>
  Fifth Case:
  </ins>

    Initial Node: NT
    Goal Node: NT
    Path: [<Node NT>]
    Cost: 0


## 🔹 Depth First Search Algorithm

  <ins>
  First Case:
  </ins>
  
    Initial Node: V
    Goal Node: SA
    Path: [<Node SA>, <Node NSW>, <Node V>]
    Cost: 2

  <ins>
  Second case:
  </ins>

    Initial Node: WA
    Goal Node: WA
    Path: [<Node WA>]
    Cost: 0

  <ins>
  Third case:
  </ins>

    Initial Node: Q
    Goal Node: Q
    Path: [<Node Q>]
    Cost: 0

  <ins>
  Fourth Case:
  </ins>

    Initial Node: SA
    Goal Node: NSW
    Path: [<Node NSW>, <Node V>, <Node SA>]
    Cost: 2

  <ins>
  Fifth Case:
  </ins>

    Initial Node: NT
    Goal Node: NT
    Path: [<Node NT>]
    Cost: 0

## 🔸 Branch and Bound Algorithm using cost as heuristic

<ins>
  First Case:
  </ins>
  
    Initial Node: V
    Goal Node: SA
    Path: [<Node SA>, <Node V>]
    Cost: 1

  <ins>
  Second case:
  </ins>

    Initial Node: WA
    Goal Node: WA
    Path: [<Node WA>]
    Cost: 0

  <ins>
  Third case:
  </ins>

    Initial Node: Q
    Goal Node: Q
    Path: [<Node Q>]
    Cost: 0

  <ins>
  Fourth Case:
  </ins>

    Initial Node: SA
    Goal Node: NSW
    Path: [<Node NSW>, <Node SA>]
    Cost: 1

  <ins>
  Fifth Case:
  </ins>

    Initial Node: NT
    Goal Node: NT
    Path: [<Node NT>]
    Cost: 0


## 🔹 Branch and Bound Algorithm using underestimation as heuristic

  <ins>
  First Case:
  </ins>
  
    Initial Node: V
    Goal Node: SA
    Path: <Node SA>, <Node Q>, <Node NSW>, <Node V>]
    Cost: 3

  <ins>
  Second case:
  </ins>

    Initial Node: WA
    Goal Node: WA
    Path: [<Node WA>]
    Cost: 0

  <ins>
  Third case:
  </ins>

    Initial Node: Q
    Goal Node: Q
    Path: [<Node Q>]
    Cost: 0

  <ins>
  Fourth Case:
  </ins>

    Initial Node: SA
    Goal Node: NSW
    Path: [<Node NSW>, <Node Q>, <Node SA>]
    Cost: 2

  <ins>
  Fifth Case:
  </ins>

    Initial Node: NT
    Goal Node: NT
    Path: [<Node NT>]
    Cost: 0