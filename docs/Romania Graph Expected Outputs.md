#  Expected outputs for differents search methods


## 🔸 Breadth First Search Algorithm

  <ins>
  First Case:
  </ins>
  
    Initial Node: A
    Goal Node: B
    Path: [<Node B>, <Node F>, <Node S>, <Node A>]
    Cost: 450

  <ins>
  Second case:
  </ins>

    Initial Node: F
    Goal Node: P
    Path: [<Node P>, <Node B>, <Node F>]
    Cost: 312

  <ins>
  Third case:
  </ins>

    Initial Node: A
    Goal Node: U
    Path: [<Node U>, <Node B>, <Node F>, <Node S>, <Node A>]
    Cost: 535

  <ins>
  Fourth Case:
  </ins>

    Initial Node: D
    Goal Node: I
    Path: [<Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node C>, <Node D>]
    Cost: 678

  <ins>
  Fifth Case:
  </ins>

    Initial Node: H
    Goal Node: R
    Path: [<Node R>, <Node P>, <Node B>, <Node U>, <Node H>]
    Cost: 381


## 🔹 Depth First Search Algorithm

  <ins>
  First Case:
  </ins>
  
    Initial Node: A
    Goal Node: B
    Path: [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]
    Cost: 733

  <ins>
  Second case:
  </ins>

    Initial Node: F
    Goal Node: P
    Path: [<Node P>, <Node B>, <Node F>]
    Cost: 312

  <ins>
  Third case:
  </ins>

    Initial Node: A
    Goal Node: U
    Path: [<Node U>, <Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]
    Cost: 818

  <ins>
  Fourth Case:
  </ins>

    Initial Node: D
    Goal Node: I
    Path: [<Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node C>, <Node D>]
    Cost: 678

  <ins>
  Fifth Case:
  </ins>

    Initial Node: H
    Goal Node: R
    Path: [<Node R>, <Node S>, <Node F>, <Node B>, <Node U>, <Node H>]
    Cost: 573


## 🔸 Branch and Bound Algorithm using cost as heuristic

  <ins>
  First Case:
  </ins>
  
    Initial Node: A
    Goal Node: B
    Path: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
    Cost: 418

  <ins>
  Second case:
  </ins>

    Initial Node: F
    Goal Node: P
    Path: [<Node P>, <Node R>, <Node S>, <Node F>]
    Cost: 276

  <ins>
  Third case:
  </ins>

    Initial Node: A
    Goal Node: U
    Path: [<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
    Cost: 503

  <ins>
  Fourth Case:
  </ins>

    Initial Node: D
    Goal Node: I
    Path: [<Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node C>, <Node D>]
    Cost: 678

  <ins>
  Fifth Case:
  </ins>

    Initial Node: H
    Goal Node: R
    Path: [<Node R>, <Node P>, <Node B>, <Node U>, <Node H>]
    Cost: 381


## 🔹 Branch and Bound Algorithm using underestimation as heuristic

  <ins>
  First Case:
  </ins>
  
    Initial Node: A
    Goal Node: B
    Path: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
    Cost: 418

  <ins>
  Second case:
  </ins>

    Initial Node: F
    Goal Node: P
    Path: [<Node P>, <Node R>, <Node S>, <Node F>]
    Cost: 276

  <ins>
  Third case:
  </ins>

    Initial Node: A
    Goal Node: U
    Path: [<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
    Cost: 503

  <ins>
  Fourth Case:
  </ins>

    Initial Node: D
    Goal Node: I
    Path: [<Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node C>, <Node D>]
    Cost: 678

  <ins>
  Fifth Case:
  </ins>

    Initial Node: H
    Goal Node: R
    Path: [<Node R>, <Node P>, <Node B>, <Node U>, <Node H>]
    Cost: 381