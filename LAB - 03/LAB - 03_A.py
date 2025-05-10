def merge(a, b):
  sorted_list = []
  i, j = 0, 0
  count = 0
  while (i < len(a)) and (j < len(b)):
    if a[i] <= b[j]:
      sorted_list.append(a[i])
      i += 1
    else:
      sorted_list.append(b[j])
      count += len(a)-i
      j += 1

  sorted_list.extend(a[i:])
  sorted_list.extend(b[j:])
  return count, sorted_list

def mergeSort(arr):
  if len(arr)<= 1: return 0, arr

  mid = len(arr)// 2
  LC, left_side = mergeSort(arr[:mid])
  RC, right_side = mergeSort(arr[mid:])
  MC, merged = merge(left_side, right_side)

  return (LC+ RC+ MC), merged

num = int(input())
arr = input().split()
arr = [int(x) for x in arr]
count, sorted_arr = mergeSort(arr)
print(count)
print(*sorted_arr)