# 깊이 우선 검색
# 함수가 날짜를 계속 점핑하면서 맨 마지막 날자까지 들어간 표값을 합이 비용
# 그 값들 중에서 가장 작은 값을 찾는다.
# 일단 쿠폰은 빼고 1일부터 5일까지 어떻게 될지 생각해보자.
# 날짜 1 2 3 4 5 6 7 8
#     1 1 1 1 1 1
#       3 x x
#       5 x x x x
#     3 x x 1 1 1
#           3 x x
#           5 x x x x
#     5 x x x x 1 1 1
#               3 x x
#               5 x x x x

import sys
sys.setrecursionlimit(100000)
# 리조트
N, M = map(int, input().split())

arrM = []
if M > 0:
    arrM = list(map(int, input().split()))

memo = {}  # for memoization

# x : 날짜 1일에서 n일까지 DFS(Depth First Search)


def dfs(day, coupon):
    if day > N:
        return 0
    # 날짜와 쿠폰 갯수로 키를 만든다.
    key = str(day) + ',' + str(coupon)

    # 메모이제이션 된 것이 있으면 그 데이터를 리턴
    if key in memo:
        return memo[key]

    # 쉬는 날이면 그 다음날의 비용을 계산을 넘긴다.
    if day in arrM:
        return 0 + dfs(day+1, coupon)

    # 표를 1일치를 사면 그 다음날 껄로 가서 비용 계산
    cost1 = 10000 + dfs(day+1, coupon)

    # 표를 2일치를 사면 다음 다음날부터 계산
    # 표를 이미 샀기 때문에 그 다음날은 어차피 계산할 비용이 0이라서 계산할 필요가 없다.
    # 이렇게 날짜를 건너뛰지 않으려면 표를 날짜 어레이에 기억해서 하는 법도 있을 건데 그럴 필요까지야.
    cost2 = 25000 + dfs(day+3, coupon+1)

    # 5일권
    cost3 = 37000 + dfs(day+5, coupon+2)

    arrCost = [cost1, cost2, cost3]
    # 쿠폰이 3장인 경우 사용하는 경우도 고려
    if coupon >= 3:
        cost4 = 0 + dfs(day+1, coupon-3)
        arrCost.append(cost4)

    cost = min(arrCost)
    memo[key] = cost
    return cost


print(dfs(1, 0))
