def pair_max(A, left, right):
  if len(A) == 1: return A[0]

  mid = len(A)// 2
  leftS = A[:mid]
  rightS= A[mid:]

  leftR = pair_max(leftS, leftS[:mid], leftS[mid:])
  rightR = pair_max(rightS, rightS[:mid], rightS[mid:])

  max_left_val = max(leftS)
  max_right_val = max(max(rightS)**2, min(rightS)**2)
  req_val = max_left_val + max_right_val

  return max(leftR, rightR, req_val)


num = int(input())
d = input().split()
d = [int(x) for x in d]

print(pair_max(d, d[:num//2], d[num//2:]))
