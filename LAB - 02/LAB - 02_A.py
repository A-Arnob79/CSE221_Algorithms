len, num = input().split()
len = int(len)
arr = input().split()
arr = [int(x) for x in arr]
flag = False

i = 0
j = len-1
while i<j:
  if (arr[i]+ arr[j]) < int(num): i+=1
  elif (arr[i]+ arr[j]) > int(num): j-=1
  else:
    print(f"{i+1} {j+1}")
    flag = True
    break
if flag == False: print(-1)