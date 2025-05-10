num, k = input().split()
sum = 0
arr = input().split()
arr = [int(x) for x in arr]
i, j = 0, 0
max_L = 0

while j< int(num):
  sum += arr[j]
  while (sum> int(k)) and (i<= j):
    sum -= arr[i]
    i+=1

  max_L = max(max_L, ((j-i)+1))
  j+=1

print(max_L)