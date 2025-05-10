num = int(input())
arr = input().split(' ')

arr = [int(x) for x in arr]

for i in range(num):
  flag = False
  for j in range(num-i-1):
    if arr[j]> arr[j+1]:
      arr[j], arr[j+1]= arr[j+1], arr[j]
      flag = True
  if flag == False:break
print(*arr)