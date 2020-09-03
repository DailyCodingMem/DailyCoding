# programmers - Lv1 - 모의고사 (2020-09-03)
# https://programmers.co.kr/learn/courses/30/lessons/42840

import sys
sys.stdin = open("programmers/[Lv1]모의고사.txt",'r')

def calculate(answers, people, len_method):
    result = 0
    # 각 사람들의 맞춘 갯수
    for i in range(len(answers)):
        if i >= len_method :
            if people[i%len_method] == answers[i]:
                result += 1
        else :
            if people[i] == answers[i]:
                result += 1
    return result

def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    score = [calculate(answers,p1,5), calculate(answers,p2,8), calculate(answers,p3,10)]
    S = max(score)
    idx = 1
    for p in score :
        if p == S :
            answer.append(idx)
        idx += 1
    
    return answer

T = int(input())
for _ in range(T):
    s = list(map(int, input().split(',')))
    
    print(solution(s))    

