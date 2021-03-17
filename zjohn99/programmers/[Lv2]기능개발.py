# programmers - Lv2 - 기능개발 (2020-09-16)
# https://programmers.co.kr/learn/courses/30/lessons/42586

import sys
sys.stdin = open("programmers/[Lv2]기능개발.txt",'r')
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    while(progresses):
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while(progresses[0] >= 100) :
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            if not progresses :
                 break
        if cnt != 0 :
            answer.append(cnt)
    
    return answer


T = int(input())
for _ in range(T):
    progresses = list(map(int, input().split()))
    speeds = list(map(int, input().split()))


    print(solution(progresses, speeds))    

