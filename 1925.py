def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def comb(n, r):
    a = factorial(n)  # 분자
    b = factorial(r) * factorial(n-r)  # 분모
    return a/b


n, r = map(int, input().split())


print(int(comb(n, r)))
