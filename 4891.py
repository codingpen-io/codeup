input()

arr = list(map(int, input().split()))

max = 0
min = 10000

for n in arr:
    if n > max:
        max = n
    if n < min:
        min = n

print(max - min)
