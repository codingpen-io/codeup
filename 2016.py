n = input()
s = input()
# print(f'{s:,}'
# 문자열을 뒤집어서 뒤에서부터 처리
s = s[::-1]

# 출력 문자열에 추가 해주는 것.
o = ''
for i in range(len(s)):
    c = s[i]
    # 3,210
    # '3' + ',' + '210'
    if i % 3 == 0 and i != 0:
        o = ',' + o
    o = c + o


print(o)
