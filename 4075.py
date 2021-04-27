l = input()
orig = l.lower()

r = ''
isPalindorme = True
for i in range(0, len(l)//2):
    if l[i] != l[len(l)-1-i]:
        isPalindorme = False
        break
    r += l[i]

if isPalindorme:
    print("Yes")
    print(r)
else:
    print("No")
    print(orig + orig[::-1])
