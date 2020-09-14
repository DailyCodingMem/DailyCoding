# programmers - Lv1 - 나누어떨어지는숫자 (2020-09-10)
# https://programmers.co.kr/learn/courses/30/lessons/12903

import sys
sys.stdin = open("programmers/[Lv1]나누어떨어지는숫자.txt",'r')

def solution(arr, divisor):
    answer = []
    arr.sort()
    for a in arr:
        if a % divisor == 0 :
            answer.append(a)
    if len(answer) == 0:
        answer.append(-1)   
    
    return answer

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    divisor = int(input())
    
    print(solution(arr, divisor))    

