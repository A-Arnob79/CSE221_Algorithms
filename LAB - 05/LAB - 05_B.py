# DFS
import sys
sys.setrecursionlimit((2* 10**5)+5)
white, grey, B = 0, 1, 2

n, m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for i in range(m):
    u = u_list[i]
    v = v_list[i]
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    adj[i].sort()

color = [white] * (n + 1)
d = [0] * (n + 1)
f = [0] * (n + 1)
time = [0]
result = []

def DFS():
    for u in range(1, n + 1):
        color[u] = white
    time[0] = 0
    for u in range(1, n + 1):
        if color[u] == white:
            DFS_Visit(u)

def DFS_Visit(u):

    color[u] = grey
    time[0] += 1
    d[u] = time[0]
    result.append(u)
    for v in adj[u]:
        if color[v] == white:
            DFS_Visit(v)

    color[u] = B
    time[0] += 1
    f[u] = time[0]

DFS()
print(' '.join(map(str, result)))

# To print discovery and finishing times:
# for i in range(1, n + 1):
# print(f"Node {i}: d = {d[i]}, f = {f[i]}")