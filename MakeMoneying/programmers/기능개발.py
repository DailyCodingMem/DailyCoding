def solution(progresses, speeds):
    days = [] # [7,3,9]
    for i in range(len(progresses)):
        day = 0
        total_day = progresses[i]
        while total_day<100:
            day += 1
            total_day = progresses[i] + day*speeds[i]
        days.append(day)
    answer = []
    # print(days )
    cnt = 1
    day = 0
    max_day = days[0]
    while day < len(days):
        if day == len(days)-1:
            answer.append(cnt)
        elif max_day < days[day+1]:
            max_day = days[day+1]
            answer.append(cnt)
            cnt = 1
        elif max_day >= days[day+1]:
            cnt += 1
        day += 1
    return answer








progresses = [93, 30, 55]
progresses = [95, 90, 99, 99, 80, 99]
progresses = [99, 99, 98, 97, 97, 96]
progresses = [99, 1]
progresses = [95, 95, 95, 95]
# progresses=[0,0,0,0]
# progresses = [40, 93, 30, 55, 60, 65]

# [2]
speeds = [1, 30, 5]
speeds = [1, 1, 1, 1, 1, 1]
speeds = [1, 99] 
speeds = [4, 3, 2, 1]
# speeds=[100,50,34,25]
# speeds = [60, 1, 30, 5 , 10, 7]
print(solution(progresses, speeds))