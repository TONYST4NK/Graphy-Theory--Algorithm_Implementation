# Graphy-Theory_Algorithms-Implementation
Coding project to implement Travelling Salesman Project, Chinese Postman Problem, and The Knight's Tour

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

