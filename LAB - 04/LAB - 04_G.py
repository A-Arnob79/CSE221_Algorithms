import math
N, Q = map(int, input().split())

G = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and math.gcd(i, j) == 1:
            G[i].append(j)

for i in range(1, N + 1):
    G[i].sort()

res = []
for _ in range(Q):
    X, K = map(int, input().split())
    if K <= len(G[X]): res.append(str(G[X][K - 1]))
    else: res.append("-1")
print("\n".join(res))