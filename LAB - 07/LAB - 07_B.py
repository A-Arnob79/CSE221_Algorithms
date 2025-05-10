import heapq

def dijkstra_A(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > (d+w):
                dist[v] = (d+w)
                heapq.heappush(heap, (dist[v], v))
    return dist

n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

alice = dijkstra_A(s, graph, n)
bob = dijkstra_A(t, graph, n)
ans = -1
best_time = float('inf')

for i in range(1, n + 1):
    if alice[i] < float('inf') and bob[i] < float('inf'):
        time = max(alice[i], bob[i])
        if time < best_time or ((time== best_time) and (i< ans)):
            best_time = time
            ans = i

if ans == -1: print(-1)
else: print(best_time, ans)