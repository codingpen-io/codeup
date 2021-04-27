n = int(input())
arr = input().split()
arr2 = []

for n in arr:
  arr2.insert(0, n)

print(''.join(arr2))