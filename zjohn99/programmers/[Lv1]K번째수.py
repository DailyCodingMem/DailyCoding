# programmers - Lv1 - k번째수 (2020-09-04)
# https://programmers.co.kr/learn/courses/30/lessons/42748

import sys
sys.stdin = open("programmers/[Lv1]K번째수.txt",'r')

def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i = commands[a][0]-1
        j = commands[a][1]
        k = commands[a][2]-1
        
        tmp = array[i:j]
        tmp.sort()
        answer.append(tmp[k])
        
    
    return answer

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    com = [list(map(int, input().split())) for _ in range(3)]
    
    print(solution(arr, com))    
