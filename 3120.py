a, b = map(int, input().split())

d = b - a

arr = [1, -1, 5, -5, 10, -10]
count = 0

while True:
    if d == 0:
        break

    min = 10000
    min_x = None
    for x in arr:
        if abs(d - x) < min:
            min = abs(d-x)
            min_x = x
    count += 1
    d -= min_x

print(count)
