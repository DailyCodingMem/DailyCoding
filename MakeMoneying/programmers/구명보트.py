def solution(people, limit):
    people.sort()
    answer = 0
    start = 0
    end = len(people)-1
    while end >= start:
        answer += 1
        if people[start] + people[end] <= limit: # 두명 실을 수 있는 경우
            start += 1
            end -= 1
        else: # 한명만 실을 경우
            end -= 1
        
    print(answer)
    return answer

people = [70, 50, 80, 50]
people = [10,20,30,40,50,60,70,80,90]
limit = 100
solution(people, limit)