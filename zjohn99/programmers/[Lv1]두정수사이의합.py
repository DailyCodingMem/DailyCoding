# programmers - Lv1 - 두정수사이의합 (2020-09-03)
# https://programmers.co.kr/learn/courses/30/lessons/42840

import sys
sys.stdin = open("programmers/[Lv1]두정수사이의합.txt",'r')

def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1) :
        answer += i
    return answer

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    
    print(solution(a, b))    

