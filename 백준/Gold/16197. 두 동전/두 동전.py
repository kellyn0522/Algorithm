from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

coins = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coins.append((i, j))

def bfs():
    q = deque()
    x1, y1 = coins[0]
    x2, y2 = coins[1]
    q.append((x1, y1, x2, y2, 0))

    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        if cnt >= 10:
            return -1

        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == '#':
                nx2, ny2 = x2, y2

            out1 = not (0 <= nx1 < n and 0 <= ny1 < m)
            out2 = not (0 <= nx2 < n and 0 <= ny2 < m)

            if out1 and out2:
                continue
            elif out1 or out2:
                return cnt + 1
            else:
                q.append((nx1, ny1, nx2, ny2, cnt + 1))

    return -1

print(bfs())
