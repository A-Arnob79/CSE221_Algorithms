from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * (n + 1)
output = 0

for i in range(1, n + 1):
    if color[i] == -1:
        Q = deque([i])
        color[i] = 0
        c1 = 1
        c2 = 0

        while Q:
            u = Q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    if color[v] == 0: c1 += 1
                    else: c2 += 1
                    Q.append(v)

        output += max(c1, c2)

print(output)