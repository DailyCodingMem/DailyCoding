def solution(k, m, score):
    answer = 0
    return answer

k =  4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
score = sorted(score, reverse=True)
answer = 0
for i in range(0, len(score), m):
    temp = score[i:m+i]
    if len(temp) == m:
        answer += min(temp) * m
print(answer)
