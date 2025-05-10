import heapq
from collections import defaultdict

def second_shortest_path():
    n, m, s, d = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    inf = float('inf')
    dist = [[inf, inf] for _ in range(n + 1)]
    dist[s][0] = 0
    pq = [(0, s)]

    while pq:
        cost, u = heapq.heappop(pq)
        for v, w in graph[u]:
            new_cost = cost + w

            if new_cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new_cost
                heapq.heappush(pq, (new_cost, v))

            elif dist[v][0] < new_cost < dist[v][1]:
                dist[v][1] = new_cost
                heapq.heappush(pq, (new_cost, v))

    result = dist[d][1]
    if result < inf: print(result)
    else: print (-1)
second_shortest_path()