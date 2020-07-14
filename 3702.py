memo = {}


def my_func(r, c):
    if r == 1:
        return 1
    if c == 1:
        return 1

    key = str(r)+":"+str(c)
    if not key in memo:
        memo[key] = my_func(r-1, c) + my_func(r, c-1)

    return memo[key]


r, c = map(int, input().split())
print(my_func(r, c) % 100000000)
