A = 5 * 60
B = 1 * 60
C = 10

arr = [A, B, C]

t = int(input())

a = t//A
t -= a * A

b = t//B
t -= b * B

c = t//C
t -= c * C

if t > 0:
    print(-1)
else:
    print(a, b, c)
