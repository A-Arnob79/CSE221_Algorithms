import sys
sys.setrecursionlimit(2 * 10**5)

N, R = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
size = [0] * (N + 1)

def dfs(start):
    stack = [(start, -1)]
    postorder = []

    while stack:
        node, parent = stack[-1]
        if node < 0:
            node = -node
            size[node] = 1

            for neighbor in adj[node]:
                if neighbor != parent:
                    size[node] += size[neighbor]
            stack.pop()
        else:
            stack[-1] = (-node, parent)

            for neighbor in adj[node]:
                if neighbor != parent:
                    stack.append((neighbor, node))
    return

dfs(R)
Q = int(input())
results = []
for _ in range(Q):
    X = int(input())
    results.append(str(size[X]))
print("\n".join(results))