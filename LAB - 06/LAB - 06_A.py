from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

in_degree = [0] * (n + 1)

for _ in range(m):
    A, B = map(int, input().split())
    adj[A].append(B)
    in_degree[B] += 1

Q = deque()
order = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        Q.append(i)

while Q:
    u = Q.popleft()
    order.append(u)
    for v in adj[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            Q.append(v)

if len(order) == n: print(*order)
else: print(-1)