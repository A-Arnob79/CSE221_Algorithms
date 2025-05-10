# BFS
from collections import deque
white, grey, B = 0, 1, 2
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for u in range(1, n + 1):
    adj[u].sort()

color = [white] * (n + 1)
dist = [-1] * (n + 1)
prev = [None] * (n + 1)


s = 1
color[s] = grey
dist[s] = 0
Q = deque()
Q.append(s)
t_order = []

while Q:
    u = Q.popleft()
    t_order.append(u)

    for v in adj[u]:

        if color[v] == white:
            color[v] = grey
            dist[v] = dist[u] + 1
            prev[v] = u
            Q.append(v)

    color[u] = B

print(' '.join(map(str, t_order)))