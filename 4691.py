n = int(input())
arrMoney = []

for i in range(n):
    dices = list(map(int, input().split()))
    dicSame = {}
    for n in dices:
        if n in dicSame:
            dicSame[n] += 1
        else:
            dicSame[n] = 1

    money = 0
    two_count = 0
    two_count_val = 0
    maxKey = 0
    for key in dicSame:
        count = dicSame[key]
        if count == 4:
            money = 50000 + key * 5000
        elif count == 3:
            money = 10000 + key * 1000
        elif count == 2:
            if two_count == 0:
                two_count = 1
                two_count_val = key
            else:
                two_count += 1
                two_count_val += key
        else:
            if key > maxKey:
                maxKey = key

    if two_count == 2:
        money = 2000 + two_count_val * 500
    elif two_count == 1:
        money = 1000 + two_count_val * 100
    elif money == 0:
        money = maxKey * 100

    arrMoney.append(money)

# print(arrMoney)
print(max(arrMoney))
