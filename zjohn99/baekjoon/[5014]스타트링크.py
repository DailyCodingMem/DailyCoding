# baekjoon - [2468]안전영역 (2020-12-02)
# https://www.acmicpc.net/problem/5014
import sys
from collections import deque
sys.stdin = open("baekjoon/[5014]스타트링크.txt",'r')

# def solution(F,S,G,U,D):
#     cnt = 0
#     st = [S]
#     if S > G and D == 0 or S < G and U == 0 or S != G and U == D:
#         return 'use the stairs'
    
#     while(st):
#         tmp = st.pop(0)
#         if tmp < G and tmp+U <= F:
#             tmp += U
#             cnt += 1
#             st.append(tmp)
#         elif tmp < G and tmp+U > F:
#             tmp -= D
#             cnt += 1
#             st.append(tmp)
#         elif tmp > G and tmp-D >= 0:
#             tmp -= D
#             cnt += 1
#             st.append(tmp)
#         elif tmp > G and tmp-D < 0:
#             tmp += U
#             cnt += 1
#             st.append(tmp)
#         elif tmp == G :
#             return cnt
#     return 'use the stairs'

def solution() :
    q = deque([S])
    state = False

    while(q) :
        x = q.popleft()
        if x == G :
            state = True
            break

        for i in (x+U, x-D):
            if 0 < i <= F and not pos[i]:
                pos[i] = pos[x] + 1
                q.append(i)
        
    if state :
        # print(pos)
        return pos[G]
    else :
        return 'use the stairs'

T = int(input())
for t in range(1, T+1):
    F, S, G, U, D = map(int, input().split())
    pos = [0] * (F+1)
    print(solution())
