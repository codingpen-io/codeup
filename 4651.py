r = ['E', 'A', 'B', 'C', 'D']
for i in range(3):
    arr = list(map(int, input().split()))
    zero_count = 0
    for n in arr:
        if n == 0:
            zero_count += 1

    print(r[zero_count])
