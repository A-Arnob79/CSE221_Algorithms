le, num = input().split()
arr = input().split()
arr = [int(x) for x in arr]
le = int(le)

def left_index(le, arr, x):
  l, r = 0, le
  while l < r:
    mid = (l + r)// 2
    if arr[mid]< x: l = mid + 1
    else: r = mid
  return l

def right_index(le, arr, y):
  l, r = 0, le
  while l < r:
    mid = (l + r)// 2
    if arr[mid]<= y: l = mid + 1
    else: r = mid
  return l

result = []
for _ in range(int(num)):
  x, y = input().split()
  x, y = int(x), int(y)
  count = (right_index(le, arr, y) - left_index(le, arr, x))
  result.append(str(count))

print("\n".join(result))