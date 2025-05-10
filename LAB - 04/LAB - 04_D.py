# D_Eucledian Path

n, m = input().split()
u = input().split()
v = input().split()
u = [int(x) for x in u]
v = [int(x) for x in v]

degree_list = [0]* (int(n)+1)
count = 0

for i in range(int(m)):
  degree_list[u[i]] += 1
  degree_list[v[i]] += 1

for x in degree_list:
  if x % 2 != 0: count += 1

if (count== 0) or (count== 2): print("YES")
else: print("NO")