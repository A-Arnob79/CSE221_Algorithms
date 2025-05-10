num = int(input())
for i in range(num):
  original = input()
  cal_str, NUM1, sign, NUM2 = original.split(' ')
  if sign == '+':
    print(int(NUM1) + int(NUM2))
  elif sign == '-':
    print(int(NUM1) - int(NUM2))
  elif sign == '*':
    print(int(NUM1) * int(NUM2))
  elif sign == '/':
    print(int(NUM1) / int(NUM2))