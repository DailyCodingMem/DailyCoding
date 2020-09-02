# programmers - Lv1 - 가운데글자가져오기 (2020-09-02)
# https://programmers.co.kr/learn/courses/30/lessons/12903

import sys
sys.stdin = open("programmers/[Lv1]가운데글자가져오기.txt",'r')

def solution(s):
    answer = ''
    if len(s)%2 == 0 : # 길이가 짝수일 때,
        answer += s[len(s)//2-1]
        answer += s[len(s)//2] 
        # s[len(s)//2-1 : len(s)//2+1]  오오
    else :
        answer += s[len(s)//2]

    return answer

T = int(input())
for _ in range(T):
    s = input()
    
    print(solution(s))    

