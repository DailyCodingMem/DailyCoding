# baekjoon - [1987]알파벳 (2020-12-15)
# https://www.acmicpc.net/problem/1987

from collections import deque
import sys
sys.stdin = open("baekjoon/[1987]알파벳.txt",'r')

def solution(y, x) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    st = deque([(y,x,1)])
    visited = [[[] for _ in range(C)] for _ in range(R)]
    visited[y][x] += mat[y][x]
    # words = deque([mat[y][x]])
    max_word = 0
    while(st) :
        y, x, cnt = st.popleft()
        if max_word < cnt :
            max_word = cnt

        # if len(visited[y][x]) < cnt :
            
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C :
                if mat[ny][nx] not in visited[y][x] and len(visited[ny][nx]) < len(visited[y][x])+1:
                    st.append((ny,nx,cnt+1))
                    visited[ny][nx] += mat[ny][nx]
                    visited[ny][nx] += visited[y][x]
        #           
        # else :
        #     st.pop()
        #     words.pop()
    
    return max_word




T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    mat = [list(map(str,input())) for _ in range(R)]
    
    print(solution(0,0))