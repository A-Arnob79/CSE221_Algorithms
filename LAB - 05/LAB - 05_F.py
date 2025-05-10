from collections import deque
def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    diamond_count = 0

    if grid[r][c] == 'D':
        diamond_count += 1

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < R and 0 <= new_y < H and not visited[new_x][new_y] and grid[new_x][new_y] != '#':
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))
                if grid[new_x][new_y] == 'D':
                    diamond_count += 1

    return diamond_count

R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False] * H for _ in range(R)]
max_diamonds = 0

for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            max_diamonds = max(max_diamonds, bfs(i, j))

print(max_diamonds)