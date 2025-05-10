# C
def fast_mod(a, b):
  c = 107
  sol = 1
  a = a % c
  while b > 0:
    if b % 2 == 1: sol = (sol*a) % c
    a = (a*a) % c
    b = (b//2)
  return sol

a, b = input().split()
print(fast_mod(int(a), int(b)))