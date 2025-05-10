def degDif(N, M, u, v):
    indegree = [0] * (N +1)
    outdegree = [0] * (N +1)
    result = [0] * N

    for i in range(M):
        outdegree[u[i]] += 1
        indegree[v[i]] += 1
    for i in range(1, N+1):
      result[i-1] = (indegree[i] - outdegree[i])
    return result

N, M = input().split()
u = input().split()
u = [int(i) for i in u]
v = input().split()
v = [int(i) for i in v]

print(*degDif(int(N), int(M), u, v))