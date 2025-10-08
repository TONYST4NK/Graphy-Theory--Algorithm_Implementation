# Chinese Postman Problem (CPP) Solver

## 🧾 Input Format

The program reads input from a text file (`input_sample.txt`) in the
following format:

    n e
    edge_id u v cost
    ...
    start_node

### Example:

    3 4
    0 1 2 10
    1 2 3 5
    2 3 1 7
    3 3 1 2
    1

Where: - `n` = number of vertices (in this example, 3) - `e` = number of
edges (in this example, 4) - Each subsequent line represents an
**edge**: - `edge_id` → an identifier for the edge - `u`, `v` →
endpoints of the edge (the graph is undirected) - `cost` → weight of the
edge - The **last line** (`1`) represents the **starting vertex**.

------------------------------------------------------------------------

## 🧮 Algorithm Explanation

This program implements the **Chinese Postman Problem (CPP)** --- also
known as the **Route Inspection Problem**.\
It finds the minimum cost required to traverse every edge of a connected
undirected graph **at least once**, returning to the starting node.

### Algorithm steps:

1.  **Parse Input:**\
    Reads and structures graph data (nodes, edges, weights).
2.  **Compute Degrees:**\
    Determines the degree of each vertex (number of edges connected to
    it).
3.  **Identify Odd-Degree Vertices:**\
    CPP requires an Eulerian circuit --- all vertices must have even
    degree.\
    Any vertex with an odd degree must be paired with another odd
    vertex.
4.  **Find Shortest Paths Between Odd Vertices:**\
    Uses **Dijkstra's algorithm** to find the shortest path cost between
    each pair of odd-degree vertices.
5.  **Compute Minimum-Cost Matching:**\
    Determines the minimal additional cost required to make all vertices
    even-degree by duplicating certain edges.
6.  **Calculate Minimum CPP Cost:**\
    Adds the total cost of all edges + minimal added cost from matching.
7.  **Output Results:**
    -   Displays degrees of vertices\
    -   Odd-degree vertices\
    -   Optimal matching pair\
    -   Added cost\
    -   **Final minimum CPP cost**

------------------------------------------------------------------------

## ⚙️ How the Code Works

### Main Steps in the Code

1.  **Input Parsing**

    ``` python
    n, e = map(int, input().split())
    for _ in range(e):
        edge_id, u, v, cost = map(int, input().split())
        edges[edge_id] = (u, v, cost)
    start = int(input())
    ```

2.  **Build Graph and Compute Degrees**

    -   The graph is stored as an adjacency list.
    -   Each vertex's degree is incremented per connected edge.

3.  **Identify Odd Vertices**

    ``` python
    odd_vertices = [v for v, deg in degrees.items() if deg % 2 != 0]
    ```

4.  **Shortest Paths (Dijkstra)**

    -   Calculates the minimum distance between each pair of odd
        vertices.

5.  **Find Minimum-Cost Matching**

    -   Finds pairs of odd-degree vertices with the smallest connection
        cost.

6.  **Calculate Total CPP Cost**

    ``` python
    cpp_cost = total_edge_cost + added_cost
    ```

------------------------------------------------------------------------

## 📤 Output Explanation

### Example Run

Input:

    3 4
    0 1 2 10
    1 2 3 5
    2 3 1 7
    3 3 1 2
    1

Output:

    === Parsed input ===
    n (declared): 3
    e (declared): 4
    start node: 1

    Total vertices (unique seen): 3
    Total edges (counted by id): 4
    Edges (id: u <-> v, weight):
      0: 1 <-> 2, cost=10
      1: 2 <-> 3, cost=5
      2: 3 <-> 1, cost=7
      3: 3 <-> 1, cost=2
    Degrees:
      1: degree = 3
      2: degree = 2
      3: degree = 3

    === Solving Chinese Postman Problem ===
    Odd degree vertices: [1, 3]
    Optimal matching pairs: (1, 3)
    Added cost to make Eulerian: 2
    Minimum CPP cost = 26

### Explanation:

-   Odd-degree vertices: 1 and 3
-   The shortest path between them = 2
-   Added cost = 2 (to make all degrees even)
-   Total edge weight = 10 + 5 + 7 + 2 = 24\
    → Final **Minimum CPP Cost = 24 + 2 = 26**

------------------------------------------------------------------------
