from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for perm in permutations(dungeons):
        hp = k
        cnt = 0
        for pm in perm:
            if hp >= pm[0]:
                hp -= pm[1]
                cnt += 1
            if cnt > answer:
                answer = cnt 
    return answer


k = 80
dungeons = [[80,20],[50,40],[30,10]]

