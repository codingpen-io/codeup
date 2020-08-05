n, k = map(int, input().split())

c = 0

girl_arr = [0]*6
boy_arr = [0]*6

for i in range(n):
    s, g = map(int, input().split())
    if s == 0:
        girl_arr[g-1] += 1
    else:
        boy_arr[g-1] += 1

for i in girl_arr:
    c += i // k
    if i % k > 0:
        c += 1

for i in boy_arr:
    c += i // k
    if i % k > 0:
        c += 1

print(c)
