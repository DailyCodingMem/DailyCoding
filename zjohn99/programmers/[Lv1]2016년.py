# programmers - Lv1 - 2016 (2020-09-05)
# https://programmers.co.kr/learn/courses/30/lessons/12901

import sys
sys.stdin = open("programmers/[Lv1]2016년.txt",'r')

def solution(a,b):
    answer = ''
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [0,31,29,31,30,31,30,31,31,30,31,30]
    result = 0
    if a >= 2:
        for i in range(a):
            result += month[i]
    result += b
    result = result % 7 - 1

    answer = days[result]    
    return answer

T = int(input())
for _ in range(T):
    a,b = input().split()
    a,b = int(a), int(b)

    print(solution(a,b))    

