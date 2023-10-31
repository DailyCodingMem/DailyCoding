def solution(k, score):
    answer = []
    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
answer = []
temp = []
for i in score:
    if len(temp) < k:
        temp.append(i)
    else:
        if min(temp) < i:
            temp.remove(min(temp))
            temp.append(i)
    answer.append(min(temp))