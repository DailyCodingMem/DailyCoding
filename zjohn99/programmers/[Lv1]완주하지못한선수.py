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

T = int(input())
for _ in range(T):
    p = list(input().split())
    c = list(input().split())

    print(solution(p,c))    

