n = int(input())
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  entry = input().split()
  #times = int(entry[0])

  for j in range(len(entry)-1):
    neighbor = int(entry[j+1])
    adj_matrix[i][neighbor] = 1

for o in adj_matrix: print(*o)