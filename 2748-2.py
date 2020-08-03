m = int(input())

n = int(input())

if n <= 0:
    print(0)
    exit()

arr = list(map(int, input().split()))

# 경우의 수 앞에 +/- 가 붙어서 생길 수 있는 조합의 갯수는 매 자리수마 +이거나 -인 경우를 계속 곱하면 나온다.
# 예. 2자리의 경우
# - -
# - +
# + -
# + +
count = 0
p = 2 ** n

# 2진수를 이용한 트릭인데 문제는 2진수가 자릿수가 맞게 오지 않는다는 점이다.
#   1 -> 001  이렇게 3자로 대등하게 맞춰야 한다.
# 100 -> 100
s = bin(p-1)
s = s[2:]  # '0b101' 에서 0b를 제거
max_length = len(s)  # 2진수의 최대 길이를 구해서 나중에 앞에 00이 없는 친구들을 더해준다.
for i in range(p):
    s = bin(i)
    s = s[2:]  # '0b101' 에서 0b를 제거
    if len(s) < max_length:
        s = '0' * (max_length - len(s)) + s
    sum = 0
    for i in range(len(s)):
        if s[i] == '0':
            sum = sum + int(arr[i])
        else:
            sum = sum - int(arr[i])
    # print(i, s, "sum", sum)
    if sum == m:
        count += 1

print(count)
