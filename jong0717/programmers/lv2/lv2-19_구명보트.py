def solution(people, limit):
    people.sort()
    answer = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        answer += 1
        if people[end] + people[start] <= limit:
            start += 1
        end -= 1
    
    return answer
