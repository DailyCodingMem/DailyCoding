def solution(bridge_length, weight, truck_weights):
    bridge = [] 
    total_weight = 0
    answer = 0
    while truck_weights:
        if len(bridge)==bridge_length:
            last = bridge.pop()
            total_weight -= last
        if truck_weights[0] + total_weight <= weight:
            new = truck_weights.pop(0)
            total_weight += new
            bridge.insert(0,new)
        elif truck_weights[0] + total_weight > weight:
            bridge.insert(0,0)
        answer += 1
    answer += bridge_length
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))