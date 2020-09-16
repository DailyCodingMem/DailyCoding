# programmers - Lv2 - 주식가격 (2020-09-15)
# https://programmers.co.kr/learn/courses/30/lessons/42584

import sys
sys.stdin = open("programmers/[Lv2]주식가격.txt",'r')

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer


T = int(input())
for _ in range(T):
    prices = list(map(int, input().split()))


    print(solution(prices))    

