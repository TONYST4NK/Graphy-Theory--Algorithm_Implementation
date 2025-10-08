# Graphy-Theory--Algorithm_Implementation
Coding project to implement Travelling Salesman Project, Chinese Postman Problem, and The Knight's Tour

## Knight's Tour

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
```
5 5
2 2
```
### Output
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
