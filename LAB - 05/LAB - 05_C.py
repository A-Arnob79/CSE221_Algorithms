# shortest path for undirected shit

from collections import deque
white, grey, B = 0, 1, 2

n, m, s, d = map(int, input().split())
adj = [[] for _ in range(n + 1)]

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

for i in range(m):
    u, v = u_list[i], v_list[i]
    adj[u].append(v)
    adj[v].append(u)

for u in range(1, n + 1):
    adj[u].sort()

color = [white] * (n + 1)
dist = [-1] * (n + 1)
prev = [None] * (n + 1)

color[s] = grey
dist[s] = 0
Q = deque([s])

while Q:
    u = Q.popleft()
    for v in adj[u]:
        if color[v] == white:
            color[v] = grey
            dist[v] = dist[u] + 1
            prev[v] = u
            Q.append(v)
    color[u] = B

if dist[d] == -1:
    print(-1)
else:
    path = []
    curr = d
    while curr != None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()

    print(dist[d])
    print(' '.join(map(str, path)))