def my_func(i, sum):
    count = 0
    if i == 0:
        if sum - arr[i] == m:
            count += 1
        elif sum + arr[i] == m:
            count += 1
    else:
        count += my_func(i-1, sum+arr[i])
        count += my_func(i-1, sum-arr[i])
    return count


m = int(input())

n = int(input())

if n > 0:
    arr = list(map(int, input().split()))
    print(my_func(n-1, 0))
else:
    print(0)
