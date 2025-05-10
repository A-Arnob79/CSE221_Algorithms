# Detect cycle
import sys
sys.setrecursionlimit(10**6)
white, grey, B = 0, 1, 2

def dfs(n, adj):
    color = [white] * (n + 1)

    def dfs_visit(u):
        color[u] = grey
        for v in adj[u]:
            if color[v] == white:
                if dfs_visit(v):
                    return True
            elif color[v] == grey:
                return True
        color[u] = B
        return False

    for u in range(1, n + 1):
        if color[u] == white:
            if dfs_visit(u):
                return "YES"
    return "NO"

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

print(dfs(n, adj))