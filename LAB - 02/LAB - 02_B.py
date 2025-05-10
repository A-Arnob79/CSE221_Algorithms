len1 = int(input())
arr1 = input().split()
len2 = int(input())
arr2 = input().split()
A = []
arr1 = [int(x) for x in arr1]
arr2 = [int(x) for x in arr2]
i, j = 0, 0

while i<len1 and j<len2:
  if arr1[i] < arr2[j]:
    A.append(arr1[i])
    i+=1
  else:
    A.append(arr2[j])
    j+=1

A.extend(arr1[i:])
A.extend(arr2[j:])
print(*A)