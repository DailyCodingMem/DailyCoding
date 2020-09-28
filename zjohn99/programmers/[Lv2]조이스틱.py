# programmers - Lv2 - 조이스틱 (2020-09-23)
# https://programmers.co.kr/learn/courses/30/lessons/42860
# 중간부분 못함.


import sys
sys.stdin = open("programmers/[Lv2]조이스틱.txt",'r')

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

