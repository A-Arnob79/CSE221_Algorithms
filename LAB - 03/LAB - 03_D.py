def fast_mod(a, b, c):
  sol = 1
  a = a % c
  while b > 0:
    if b % 2 == 1: sol = (sol*a) % c
    a = (a*a) % c
    b = (b//2)
  return sol

def calc_sum(a, n, m):
  if a == 1: return n % m
  m = m *(a-1)
  a_n = fast_mod(a, n, m)
  numerator = (a *(a_n - 1)) % m
  return (numerator //(a - 1)) % m

num = int(input())
output = []

for _ in range(num):
  a, n, m = input().split()
  x = calc_sum(int(a), int(n), int(m))
  output.append(str(x))

print('\n'.join(output))