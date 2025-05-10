def find_first_one(S):
  l = 0
  r = (len(S)-1)
  index = -1

  while l <= r:
    mid = (l+ r)// 2
    if S[mid]== '1':
      index = mid
      r =(mid - 1)
    else: l = (mid + 1)

  if index == -1: return -1
  else: return index + 1

num = int(input())
sol = []

for _ in range(num):
  d = input()
  k = find_first_one(d)
  sol.append(str(k))

print("\n".join(sol))