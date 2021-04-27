
a = 4
a1 = ''

while a > 0:
  a1 = str(a%2) + a1
  a = a//2

print(a1)