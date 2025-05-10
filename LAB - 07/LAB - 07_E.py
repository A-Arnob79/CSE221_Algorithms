import heapq
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(m):
        graph[u[i]].append((v[i], w[i]))

    INF = float('inf')
    dist = [[INF, INF] for _ in range(n+1)]
    pq = []
    heapq.heappush(pq, (0, 1, -1))
    dist[1][0] = 0
    dist[1][1] = 0

    while pq:
        cost, node, last_check = heapq.heappop(pq)

        for N, w in graph[node]:
            curr_check = (w % 2)

            if last_check == -1 or curr_check != last_check:
                if (cost + w) < dist[N][curr_check]:
                    dist[N][curr_check] = (cost + w)
                    heapq.heappush(pq, (cost+w, N, curr_check))

    ans = min(dist[n][0], dist[n][1])
    print(ans if ans != INF else -1)
solve()