def bst_sort(arr):
  if len(arr)== 0: return []

  mid = (len(arr)-1) // 2
  leftS = bst_sort(arr[:mid])
  rightS = bst_sort(arr[mid+1:])

  return [arr[mid]] + leftS + rightS

num = int(input())
arr = input().split()
arr = [int(x) for x in arr]

ans = bst_sort(arr)
print(*ans)