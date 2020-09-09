# programmers - Lv1 - 문자열을정수로바꾸기 (2020-09-08)
# https://programmers.co.kr/learn/courses/30/lessons/12925

import sys
sys.stdin = open("programmers/[Lv1]문자열을정수로바꾸기.txt",'r')

def solution(s):
    answer = 0
    if s[0] == '-':
        answer -= int(s[1:])
    else :
        if s[0] == '+':
            answer += int(s[1:])
        else :
            answer = int(s[:])
    
    return answer

T = int(input())
for _ in range(T):
    s = input()
    
    print(solution(s))    


# 그냥 int 로 바꿔줘도 됌