a = input()
b = input()
d = b.split(' ')
d = d[-1::-1]

n, k = a.split(' ')
for j in range((int(n)- int(k)), len(d), 1):
  print(d[j], end = ' ')