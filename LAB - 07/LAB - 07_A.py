import heapq
n, m, s, d = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(m): graph[u[i]].append((v[i], w[i]))

dist = [float('inf')] * (n + 1)
prev = [-1] * (n + 1)
dist[s] = 0
heap = [(0, s)]

while heap:
    cost, node = heapq.heappop(heap)
    if cost > dist[node]: continue
    for N, weight in graph[node]:
        if dist[N] > dist[node] + weight:
            dist[N] = dist[node] + weight
            prev[N] = node
            heapq.heappush(heap, (dist[N], N))

if dist[d] == float('inf'): print(-1)
else:
    print(dist[d])
    path = []
    while d != -1:
        path.append(d)
        d = prev[d]
    print(*path[::-1])