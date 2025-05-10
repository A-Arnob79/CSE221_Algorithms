n, m = input().split()
n = int(n)
adj_list = {i: [] for i in range(1, n+1)}
c = 1
u = input().split()
v = input().split()
w = input().split()
u = [int(i) for i in u]
v = [int(i) for i in v]
w = [int(i) for i in w]
for i in range(int(m)):
  adj_list[int(u[i])].append((v[i], w[i]))

for u, v in adj_list.items():
  print(u,':', *v)