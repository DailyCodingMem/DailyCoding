# programmers - Lv2 - 다리를 지나는 트럭 (2020-09-15)
# https://programmers.co.kr/learn/courses/30/lessons/42583

import sys
sys.stdin = open("programmers/[Lv2]다리를지나는트럭.txt",'r')
from collections import deque

def solution(bridge_length, weight, truck_weights):
    drive_weight = deque() # 다리에 운전중인 트럭들의 무게
    drive_len = deque() # 다리에 운전중인 트럭들의 위치

    drive_weight.append(truck_weights.pop(0))  
    drive_len.append(1) 

    answer = 1 # 총 시간

    while(drive_weight):
        
        if drive_len[0] >= bridge_length :  # 맨 앞의 트럭이 다리를 건넜을때,
            drive_len.popleft()
            drive_weight.popleft()

        for i in range(len(drive_len)): # 트럭의 위치를 한칸씩 증가
            drive_len[i] += 1
            
        if len(truck_weights) > 0 : # 대기중인 트럭 있는지 여부
            if truck_weights[0] + sum(drive_weight) <= weight: # 대기중 첫 트럭과 운행중 트럭의 합이 weight가 걸리는지
                drive_len.append(1)
                drive_weight.append(truck_weights.pop(0))
                
        answer += 1    
    
    return answer


T = int(input())
for _ in range(T):
    bridge_length, weight = map(int, input().split())
    truck_weights = list(map(int, input().split()))


    print(solution(bridge_length, weight, truck_weights))    

