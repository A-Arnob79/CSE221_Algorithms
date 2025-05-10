Node, Edge = input().split()
N = int(Node)
adj_matrix = [[0 for o in range(N)] for o in range(N)]

for _ in range(int(Edge)):
    u, v, w = map(int, input().split())
    adj_matrix[u-1][v-1] = w

for i in range(len(adj_matrix)): print(*adj_matrix[i])