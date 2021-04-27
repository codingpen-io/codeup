km = int(input())
days = int(input())

# 1~10, 11~20 을 / 나누기 연산을 이용하기 위해서 -1씩 쉬프트를 한다.

if km >= 120 and days > 1:
    car = (int((km-1)/10) + 1) * 1000
    # 숙박을 한다.
    sleep = (days-1) * 40000
    il = min([15, days]) * 20000 * 0.5
    if days > 15:
        il += min([days - 15, 15]) * 20000 * 0.5 * 0.9
    if days > 30:
        il += min([days-30, 30]) * 20000 * 0.5 * 0.8
    if days > 61:
        il += (days-60) * 20000 * 0.5 * 0.7
    eat = ((days-1)*3 + 1)*5000
else:
    car = (int((km-1)/10) + 1) * days * 1000
    sleep = 0
    il = days * 20000
    eat = days * 5000
    

# print('숙박', sleep)
# print('교통', car)
# print('식비', eat)
# print('일비', il)

print(int(sleep + car + il + eat))

# 테스트 값 정답
# 125 1 38000 
# 66 20 640000
# 133 90 5649000