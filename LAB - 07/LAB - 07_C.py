import heapq

def find_min_danger(N, M, roads):
    adj = [[] for _ in range(N + 1)]
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))

    INF = float('inf')
    danger = [INF] * (N + 1)
    danger[1] = 0
    pq = [(0, 1)]

    while pq:
        current_danger, u = heapq.heappop(pq)
        if current_danger > danger[u]: continue

        for v, w in adj[u]:
            new_danger = max(current_danger, w)

            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(pq, (new_danger, v))

    result = []
    for d in danger[1:]:
        if d != INF: result.append(d)
        else: result.append(-1)
    return result

N, M = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(M)]
result = find_min_danger(N, M, roads)
print(" ".join(map(str, result)))