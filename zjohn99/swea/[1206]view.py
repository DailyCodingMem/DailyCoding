# swea - [1206]view (2020-09-02)
# https://codeup.kr/problem.php?id=1164

import sys
sys.stdin = open("swea/[1206]view.txt",'r')

T = int(input())
for t in range(1, T+1):
    len_b = int(input())
    building = list(map(int, input().split()))
    
    view = 0
    i = 1
    for b in range(2, len_b-2, i):
        side_view = max(building[b-2],building[b-1],building[b+1],building[b+2])
        # 빌딩 기준 양 옆2칸 범위에 가장 큰 빌딩 층수
        if side_view < building[b] : # 빌딩이 양 옆 층수보다 컷을 때, 조망권 있을 시
            view += building[b]-side_view
            i = 3
            # 조망권이 있으면 그 옆 2칸은 조망권이 없으므로 계산할 필요가 없다. 그러므로 3칸 건너뜀
        else :
            i = 1
            # 조망권이 없으면 한칸씩 이동해서 계산해줘야함.
    print("#{0} {1}".format(t, view))
