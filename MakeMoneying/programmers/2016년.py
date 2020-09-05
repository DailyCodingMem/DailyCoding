def solution(a,b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0
    a-=1
    for i in range(a):
        days += month[i]
    days += b
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    answer = week[days%7]
    print(days)
    return answer

a,b = map(int,input().split())
print(solution(a,b))