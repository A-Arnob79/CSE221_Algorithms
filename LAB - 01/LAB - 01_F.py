num = int(input())
roll = input().split()
roll = [int(x) for x in roll]
M = input().split()
M = [int(x) for x in M]

S = []
for i in range(num): S.append((M[i], roll[i]))

swaps = 0
for i in range(num):
  max = i
  for j in range(i+1, num):
      if S[j][0] > S[max][0] or (S[j][0] == S[max][0] and S[j][1] < S[max][1]): max = j
  if max!= i:
    S[i], S[max] = S[max], S[i]
    swaps += 1

print(f'Minimum swaps: {swaps}')
for m, r in S: print(f"ID: {r} Mark: {m}")