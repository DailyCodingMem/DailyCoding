# baekjoon - [9205]맥주마시면서걸어가기 (2020-12-01)
# https://www.acmicpc.net/problem/9205
import sys
sys.stdin = open("baekjoon/[9205]맥주마시면서걸어가기.txt",'r')

def solution():
    # 방문한 곳을 체크하기 위한 배열을 선언
    c_st = []
    st = [(home[0],home[1])]

    while(st) :
        y,x = st.pop(0)
        
        if abs(y-rock[0]) + abs(x-rock[1]) <= 1000:
            return 'happy'

        for sy,sx in store :
            dist = abs(y-sy) + abs(x-sx)
            if dist <= 1000 :
                # 방문했는지 여부 검사
                if (sy,sx) not in c_st :
                    st.append((sy,sx))
                    c_st.append((sy,sx))
    
    return 'sad'


T = int(input())
for t in range(1, T+1):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    rock = list(map(int, input().split()))

    print(solution())