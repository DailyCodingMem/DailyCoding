def solution(bridge_length, weight, truck):
    answer = 0
    q = [0] * bridge_length
    while q:
        answer += 1
        q.pop(0)
        if truck:
            if sum(q) + truck[0] <= weight:
                q.append(truck.pop(0))
            else:
                q.append(0)
    return answer
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))