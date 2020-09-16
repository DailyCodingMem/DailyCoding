def Oseyo(bridge,weight,truck_weights,total_weight):
    for i in range(len(bridge)-1,-1,-1):
        if i==len(bridge)-1 and bridge[-1]: # i가 마지막 자리에 있을 때
            last = bridge[i]
            bridge[i] = bridge[i-1]
            bridge[i-1] = 0
            total_weight -= last
        elif i and bridge[i-1]: # i가 0 이전까지, bridge[i-1]이 존재할 때
            bridge[i] = bridge[i-1]
            bridge[i-1] = 0
        elif not i: # i가 0이면
            if total_weight+truck_weights[0]<=weight:
                A = truck_weights.pop(0)
                bridge[i] = A # 트럭 앞에 A 설치
                total_weight += A
            else: bridge[0] = 0
    return bridge,total_weight

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length # [0,0]
    answer = 0
    total_weight = 0
    while truck_weights:
        answer += 1
        birdge,total_weight = Oseyo(bridge,weight,truck_weights,total_weight)
    answer += bridge_length
    print(answer)
    return answer

bridge_length  = 100
bridge_length  = 4
weight = 100
weight = 10
truck_weights = [10,10,10,10,10,10,10,10,10,10]
truck_weights = [7, 4, 5, 6]
solution(bridge_length,weight,truck_weights)
answer = 8