memo = {}

def super_sum(k, n):
    # print('k', k, 'n', n)
    if k == 0:
        return n
    sum = 0
    for i in range(1, n+1):
        key = str(k-1)+str(i)
        if not key in memo:
            memo[key] = super_sum(k-1, i)
        sum += memo[key]

    return sum

while True:
    try:
        k, n = map(int, input().split())
        print(super_sum(k, n))
    except Exception:
        break
