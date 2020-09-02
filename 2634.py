    import sys
    Money = int(input())
    N = int(input())
    Coins = list(map(int, input().split()))

    # 동전이 배수이냐 아니냐의 따라서 문제가 달라진다.
    # 배수면 아래의 방식으로 쉽게 풀린다. 그렇지 않을 경우
    # 다른 경우를 탐색을 해봐야 한다.
    '''
    Coins.reverse()
    count = 0
    for n in Coins:
        r = Money // n
        Money -= r * n
        count += r
        if Money == 0:
            break

    print(count)
    '''

    # m : 현재 까지 동전으로 만든 돈, n 탐색의 깊이
    sys.setrecursionlimit(100000)


    def solve(m, d):
        if m > Money:
            return -1
        if m == Money:
            return d

        arr = []
        for n in Coins:
            r = solve(m + n, d+1)
            if r > 0:
                arr.append(solve(m + n, d+1))
        return min(arr)


    print(solve(0, 0))
