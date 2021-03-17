def solution(priorities, location):
    List = []
    for i in range(len(priorities)):
        List.append((priorities[i],i))
    answer = 0
    while True:
        priority, idx = List.pop(0)
        for i in range(len(List)):
            if priority < List[i][0]:
                List.append((priority,idx))
                break
        else:
            answer += 1
            if idx == location:
                return answer

    return answer

priorities = [2, 1, 3, 2]
priorities = [1, 1, 9, 1, 1, 1]

location = 2
location = 0

print(solution(priorities, location))