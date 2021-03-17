from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    d = deque(truck_weights)
    passing = deque()
    passing_sum = 0

    while d:
        # print(d)
        # print(passing)
        truck = d.popleft()
        if len(passing) == bridge_length:
            tmp = passing.popleft()
            passing_sum -= tmp
        if passing_sum + truck <= weight:
            passing.append(truck)
            passing_sum += truck
            answer += 1
        else:
            passing.append( 0)
            answer += 1
            d.appendleft(truck)

    return answer