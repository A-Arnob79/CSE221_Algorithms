import sys
from collections import deque
from array import array
input = sys.stdin.readline

def solve():
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x1 == x2 and y1 == y2:
        print(0)
        return

    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    visited = [array('b', [0]*N) for _ in range(N)]
    visited[x1][y1] = 1

    q = deque()
    q.append((x1, y1, 0))

    while q:
        x, y, d = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if nx == x2 and ny == y2:
                    print(d + 1)
                    return
                visited[nx][ny] = 1
                q.append((nx, ny, d + 1))
    print(-1)

solve()