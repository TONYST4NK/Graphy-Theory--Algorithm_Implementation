# Graphy-Theory_Algorithms-Implementation
Coding project to implement Travelling Salesman Project, Chinese Postman Problem, and The Knight's Tour
### Group 5
Ardian Saptaguna Yudistira (5025241079)

Dzaky Hasbullah Wahyudi (5025211264)

Amstrong Roosevelt Zamzami(5025211191)

## Knight's Tour
The Knight's Tour problem is the mathematical problem to create a program that creates a sequence of moves of a knight on a chessboard that the knight visits every square exactly once.

### Code
C++
```
#include <bits/stdc++.h>
using namespace std;

int N, M;                  // Board dimensions
int sx, sy;                // Starting position
vector<vector<int>> board; // Stores move order
vector<pair<int,int>> path; // Stores the path of the knight

// All 8 possible moves of a knight
int dx[8] = { 2, 1, -1, -2, -2, -1, 1, 2 };
int dy[8] = { 1, 2,  2,  1, -1, -2,-2,-1 };

// Check if move is inside board and not yet visited
bool isSafe(int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < M && board[x][y] == -1);
}

// Backtracking function
bool solveKT(int x, int y, int moveCount) {
    // If all squares are visited
    if (moveCount == N * M) return true;

    // Try all next moves
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (isSafe(nx, ny)) {
            board[nx][ny] = moveCount;
            path.push_back({nx, ny});

            if (solveKT(nx, ny, moveCount + 1))
                return true;

            // Backtrack
            board[nx][ny] = -1;
            path.pop_back();
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    cin >> sx >> sy;

    board.assign(N, vector<int>(M, -1));

    // Starting square
    board[sx][sy] = 0;
    path.push_back({sx, sy});

    if (solveKT(sx, sy, 1)) {
        // Print path
        for (auto &p : path)
            cout << p.first << " " << p.second << "\n";
    } else {
        cout << "No solution found\n";
    }

    return 0;
}
```
### Input
first line defines the size of the chessboard
second line defines the starting position of the knight (coordinate)
```
5 5
2 2
```
### Output
It will be the coordinates the knight will go until it visit all squares in the chessboard
```
2 2
4 1
2 0
0 1
1 3
3 4
4 2
3 0
1 1
0 3
2 4
4 3
3 1
1 0
0 2
1 4
3 3
2 1
4 0
3 2
4 4
2 3
0 4
1 2
0 0
```
### Explanation
The algorith used for this code is backtracking (DFS). Backtracking is an algorithmic technique for problem solving where a solution is found incrementally by doing different options and undoing them if leads to a dead end. The knight will start from the given position. It marks the current position as visited. At the current position, the knight tries all 8 possible knight moves. When the a move leads toa valid unvisited position, it will move there and repeat. If the knight finds a dead end, it will backtrack and try a different move. If all N x M squares have been visited, then the knight's tour is complete.

#### a. Initialization
C++
```
#include <bits/stdc++.h>
using namespace std;

int N, M;                  // Board dimensions
int sx, sy;                // Starting position
vector<vector<int>> board; // Stores move order
vector<pair<int,int>> path; // Stores the path of the knight

// All 8 possible moves of a knight
int dx[8] = { 2, 1, -1, -2, -2, -1, 1, 2 };
int dy[8] = { 1, 2,  2,  1, -1, -2,-2,-1 };
```
Board[x][y] is the order where the knight visits position (x,y). Unvisited is marked -1. path stores the sequence to late output. The knight in a chess board moves in an L-shaped where there 2 steps in one direction and 1 step perpendicular.

#### b. Boolean functions
C++
```
bool isSafe(int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < M && board[x][y] == -1);
}

bool solveKT(int x, int y, int moveCount) {
    if (moveCount == N * M) return true; // All squares visited

    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (isSafe(nx, ny)) {
            board[nx][ny] = moveCount;          // Mark as visited
            path.push_back({nx, ny});          // Record move

            if (solveKT(nx, ny, moveCount + 1)) // Recursive call
                return true;                    // Found solution

            board[nx][ny] = -1;                 // Undo (backtrack)
            path.pop_back();                    // Remove from path
        }
    }
    return false; // No move works from here
}
```
solveKT boolean function recursively tries all 8 knight moves. It uses backtracking to explore different paths. It will return true if there is a valid solution and it will return false if there are no valid moves. The isSafe boolean function is used to check if the move is valid or not.

#### c. Main
C++
```
cin >> N >> M;
cin >> sx >> sy;

board.assign(N, vector<int>(M, -1)); // Initialize board
board[sx][sy] = 0;                    // Starting square
path.push_back({sx, sy});             // Add start to path

if (solveKT(sx, sy, 1)) {             // Start search
    for (auto &p : path)
        cout << p.first << " " << p.second << "\n";
} else {
    cout << "No solution found\n";
}
```
This function will read the board size and starting position. The initialized board is marked as unvisited(-1). The knight is placed at the starting position. Main function will call the recursive solver. If a tour exists then it will print the full path, if not then it will print “No solution found”.


## Traveling Salesmen Problem
The Traveling Salesman Problem (TSP) is a classic optimization problem in computer science and mathematics.

### Code
C++
```
#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;

int n, e, start;
vector<vector<int>> graph;   // graph[u][v] = cost or INF
vector<vector<int>> edgeId;  // edgeId[u][v] = edge id connecting u-v
vector<vector<int>> dp;      // dp[mask][pos] = best cost
vector<vector<int>> nextNode;// nextNode[mask][pos] = best next city

int tsp(int mask, int pos) {
    if (mask == (1 << n) - 1) {
        return (graph[pos][start] >= INF) ? INF : graph[pos][start];
    }
    if (dp[mask][pos] != -1) return dp[mask][pos];

    int bestCost = INF;
    int bestNext = -1;
    int bestEdge = INT_MAX; // tie-break by smallest edge id

    for (int city = 0; city < n; ++city) {
        if (!(mask & (1 << city)) && graph[pos][city] < INF) {
            int rec = tsp(mask | (1 << city), city);
            if (rec >= INF) continue;
            int tot = graph[pos][city] + rec;

            int curEdge = edgeId[pos][city];
            if (tot < bestCost ||
               (tot == bestCost && curEdge < bestEdge) ) {
                bestCost = tot;
                bestNext = city;
                bestEdge = curEdge;
            }
        }
    }

    nextNode[mask][pos] = bestNext;
    return dp[mask][pos] = bestCost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    cin >> e;

    graph.assign(n, vector<int>(n, INF));
    edgeId.assign(n, vector<int>(n, -1));

    for (int i = 0; i < e; ++i) {
        int id, a, b, cost;
        cin >> id >> a >> b >> cost;
        a--; b--; // input is 1-based nodes per examples
        if (cost < graph[a][b]) {
            graph[a][b] = graph[b][a] = cost;
            edgeId[a][b] = edgeId[b][a] = id;
        }
    }

    cin >> start;
    start--;

    dp.assign(1 << n, vector<int>(n, -1));
    nextNode.assign(1 << n, vector<int>(n, -1));

    int minCost = tsp(1 << start, start);

    if (minCost >= INF) {
        cout << "Cost: -1\nRoute:\n";
        return 0;
    }

    cout << "Cost: " << minCost << "\n";

    // reconstruct route edges using nextNode
    vector<int> routeEdges;
    int mask = 1 << start;
    int pos = start;
    while (true) {
        int nxt = nextNode[mask][pos];
        if (nxt == -1) break;
        routeEdges.push_back(edgeId[pos][nxt]);
        mask |= (1 << nxt);
        pos = nxt;
    }
    // add final closing edge back to start
    if (graph[pos][start] < INF) routeEdges.push_back(edgeId[pos][start]);

    cout << "Route: ";
    for (size_t i = 0; i < routeEdges.size(); ++i) {
        cout << routeEdges[i];
        if (i + 1 < routeEdges.size()) cout << ", ";
    }
    cout << "\n";
    return 0;
}
```

### Input
```
3
4
0 1 2 10
1 2 3 5
2 3 1 7
3 3 1 2
1
```

### Output
```
Cost: 17
Route: 0, 1, 3
```

### Explanation
This program solves the Traveling Salesman Problem (TSP) using Dynamic Programming with Bitmasking in C++.
It finds the minimum cost route that visits all nodes exactly once, starting from a given node.

### Input Format
```
N
M
u v c x
u v c x
...
start
```
N → Number of vertices
M → Number of edges
Each edge line:
    u v c x
        - u → start node (0-based)
        - v → end node
        - c → cost or distance
        - x → extra value (ignored)
start → starting node (1-based index)

### Output Format
```
Cost: <minimum cost>
Route: <route of nodes>
```
### Example Input
```
3
4
0 1 2 10
1 2 3 5
2 3 1 7
3 3 1 2
1
```
### Example Output
```
Cost: 17
Route: 0, 1, 3
```
### How It Works
1. Graph Representation
    - The graph is stored as an adjacency matrix.
    - graph[i][j] holds the cost from node i to node j.

2. Dynamic Programming with Bitmask
    - Each DP state represents which nodes have been visited.
    - dp[mask][i] = minimum cost to reach node i with visited nodes in mask.
3. Transition Formula
```
dp[nextMask][j] = min(dp[nextMask][j], dp[mask][i] + graph[i][j])
```
Move from node i to node j if j has not been visited.

4. Path Reconstruction
    - A parent table keeps track of the previous node.
    - The final path is reconstructed backward from the last node.

### 1. Input Handling
```
int n, e;
cin >> n >> e;
```
- n = number of nodes
- e = number of edges

Then the program reads all edges:
```
for (int i = 0; i < e; i++) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    graph[b-1][c-1] = d;
    graph[c-1][b-1] = d; // undirected graph
}
```
Each line represents:
```
<edge_name> <from_node> <to_node> <cost>
```
Example:
1 2 3 5 → means there’s an edge between node 2 and 3 with cost 5.
The program stores this cost in an adjacency matrix called graph.

### 2. Dynamic Programming Setup
Define a DP table:
```
vector<vector<int>> dp(1 << n, vector<int>(n, INF));
```
Here:
- 1 << n → number of possible visited sets of nodes (using bitmask)
- dp[mask][i] → minimum cost to reach node i after visiting the nodes in mask.

Example:
- mask = 0111 → means nodes {0,1,2} are visited.
- dp[0111][2] → means the minimum cost to end at node 2 after visiting nodes 0, 1, and 2.

Also keep a parent table to help rebuild the route later:
```
vector<vector<int>> parent(1 << n, vector<int>(n, -1));
```

### 3. Base Case
We start at the given starting node:
```
dp[1 << start][start] = 0;
```
That means:
The cost to start at the starting node, having only visited that node, is 0.

### 4. Transition (Main DP Loop)
```
for (int mask = 0; mask < (1 << n); mask++) {
    for (int u = 0; u < n; u++) {
        if (!(mask & (1 << u))) continue;
        for (int v = 0; v < n; v++) {
            if (mask & (1 << v) || graph[u][v] == INF) continue;
            int nextMask = mask | (1 << v);
            if (dp[nextMask][v] > dp[mask][u] + graph[u][v]) {
                dp[nextMask][v] = dp[mask][u] + graph[u][v];
                parent[nextMask][v] = u;
            }
        }
    }
}
```
This loop tries to go from each visited node u to every unvisited node v :
    - mask keeps track of which nodes have been visited.
    - If we move from u to v, we update the cost for that new visited state (nextMask).
    - The parent table is updated so we can reconstruct the path later.

### 5. Finding the Minimum Cost
After all subsets are checked, we find the best cost that returns to the start:
```
int endMask = (1 << n) - 1;
int minCost = INF, lastNode = -1;

for (int i = 0; i < n; i++) {
    if (graph[i][start] != INF && dp[endMask][i] + graph[i][start] < minCost) {
        minCost = dp[endMask][i] + graph[i][start];
        lastNode = i;
    }
}
```
This step ensures the route is complete (visits all nodes and returns home).

### 6. Route Reconstruction
We trace back using the parent table:
```
vector<int> route;
int mask = endMask;
int curr = lastNode;

while (curr != -1) {
    route.push_back(curr);
    int temp = parent[mask][curr];
    mask ^= (1 << curr);
    curr = temp;
}

reverse(route.begin(), route.end());
```
This reconstructs the route in reverse order, from the end node back to the start.

### 7. Output
Finally, the result is printed:
```
cout << "Cost: " << minCost << endl;
cout << "Route: ";
for (int i = 0; i < route.size(); i++) {
    cout << route[i];
    if (i != route.size() - 1) cout << ", ";
}
cout << endl;
```