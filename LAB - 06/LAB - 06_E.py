from collections import deque
def bfs(s, n, adj):
    dist = [-1] * (n + 1)
    dist[s] = 0
    Q = deque([s])
    farthest_node = s
    max_dist = 0

    while Q:
        node = Q.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                Q.append(neighbor)
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_dist, dist

N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

farthest_node_fs, max_dist_fs, dist_fs = bfs(1, N, adj)
farthest_node, max_dist, dist = bfs(farthest_node_fs, N, adj)
print(max_dist)
print(farthest_node_fs, farthest_node)