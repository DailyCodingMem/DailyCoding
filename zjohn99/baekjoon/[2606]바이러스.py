# baekjoon - [2606]바이러스 (2020-10-18)
# https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open("baekjoon/[2606]바이러스.txt",'r')

def solution(start) :
    visited = [False for _ in range(com+1)]
    st = [start]
    cnt = 0
    visited[start] = True
    while(st) :
        s = st.pop()

        for i in dic[s] :
            if visited[i] == False :
                st.append(i)
                cnt += 1
                visited[i] = True

    return cnt

T = int(input())
for t in range(1, T+1):
    com = int(input())
    n = int(input())
    dic = {}
    for i in range(n) :
        a, b = map(int, input().split())
        if a in dic :
            dic[a] += [b]
        else :
            dic[a] = [b]
        if b in dic :
            dic[b] += [a]
        else :
            dic[b] = [a]
    
    print(solution(1))