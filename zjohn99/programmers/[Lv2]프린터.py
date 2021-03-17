# programmers - Lv2 - 프린터 (2020-09-16)
# https://programmers.co.kr/learn/courses/30/lessons/42587

import sys
sys.stdin = open("programmers/[Lv2]프린터.txt",'r')
def solution(priorities, location):
    answer = 0
    idx = []
    cnt = 0
    L = len(priorities)
    for i in range(L):
        idx.append(i)
    info = list(zip(priorities, idx))
    while(info) :
        if info[0][0] == max(priorities) :
            cnt += 1
            if info[0][1] == location :
                answer = cnt
                break
            info.pop(0)
            priorities.pop(0)
        else :
            info.append(info.pop(0))
            priorities.append(priorities.pop(0))
            
    return answer


T = int(input())
for _ in range(T):
    priorities = list(map(int, input().split()))
    weight = int(input())


    print(solution(priorities, weight))    

