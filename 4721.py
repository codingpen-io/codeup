n = int(input())

total_scores = [0, 0, 0]
three_scores = [0, 0, 0]
two_scores = [0, 0, 0]

for i in range(n):
    lines = list(map(int, input().split()))
    for j in range(len(lines)):
        total_scores[j] += lines[j]
        if lines[j] == 3:
            three_scores[j] += 1
        elif lines[j] == 2:
            two_scores[j] += 1

max_score = max(total_scores)

# 구글 검색  python find value in list 
max_count = total_scores.count(max_score)
max_index = 0

if max_count == 1:
    max_index = total_scores.index(max_score) + 1
else:
    max_three = max(three_scores)
    max_three_count = three_scores.count(max_three)
    if max_three_count == 1:
        max_index = three_scores.index(max_three) + 1
    else:
        max_two = max(two_scores)
        max_two_count = two_scores.count(max_two)
        if max_two_count == 1:
            max_index = three_scores.index(max_two) + 1
            
print(max_index, max_score)
