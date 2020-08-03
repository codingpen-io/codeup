n = int(input())
# i | j 0 1 2
# --+--------
# 0 |   1 2 3
# 1 |   4 5 6
# 2 |   7 8 9

for i in range(n):
    for j in range(n):
        print((n-i) + n*j, end=" ")
    print()
