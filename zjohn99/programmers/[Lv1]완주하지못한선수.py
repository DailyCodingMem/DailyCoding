# programmers - Lv1 - 완주하지못한선수 (2020-09-06)
# https://programmers.co.kr/learn/courses/30/lessons/42576

import sys
sys.stdin = open("programmers/[Lv1]완주하지못한선수.txt",'r')

def solution(participant, completion):
    answer = ''
    dic_p = {}
    for p in participant:
        if p in dic_p.keys():
            dic_p[p] += 1
        else :
            dic_p[p] = 1
    for c in completion :
        if dic_p[c] :
            dic_p[c] -= 1
    
    for key in dic_p.keys() :
        if dic_p[key] != 0:
            answer = key
            return answer

# 시간초과
# def solution(participant, completion):
#     check = [False for _ in range(len(participant))]
    
#     for c in completion :
#         for p in range(len(participant)):
#             if c == participant[p] and check[p] == False:
#                 check[p] = True
#                 break
#     idx = check.index(False)
#     answer = participant[idx]
        
#     return answer

## 다른 사람 풀이
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]


T = int(input())
for _ in range(T):
    p = list(input().split())
    c = list(input().split())

    aa = [False for _ in range(len(p))]
  
    print(aa)
    print(solution(p,c))    

