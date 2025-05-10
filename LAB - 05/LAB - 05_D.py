from collections import deque
white, grey, B = 0, 1, 2

def bfs(start, adj, n):
    color = [white] * (n + 1)
    dist = [-1] * (n + 1)
    prev = [None] * (n + 1)

    color[start] = grey
    dist[start] = 0
    Q = deque()
    Q.append(start)

    while Q:
        u = Q.popleft()

        for v in adj[u]:
            if color[v] == white:
                color[v] = grey
                dist[v] = dist[u] + 1
                prev[v] = u
                Q.append(v)

        color[u] = B

    return dist, prev

def path(curr, prev):
    way = []
    while curr != None:
        way.append(curr)
        curr = prev[curr]
    return way[::-1]


n, m, s, d, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
for u in range(1, n + 1):
    adj[u].sort()

dist_s, prev_s = bfs(s, adj, n)
dist_k, prev_k = bfs(k, adj, n)

if dist_s[k] == -1 or dist_k[d] == -1: print(-1)
else:
    p = path(d, prev_k)
    P = path(k, prev_s) + p[1:]
    print(len(P)-1)
    print(' '.join(map(str, P)))