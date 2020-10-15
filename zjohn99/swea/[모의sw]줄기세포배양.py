# swea - [모의sw]줄기세포배양 (2020-10-14)
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open("swea/[모의sw]줄기세포배양.txt",'r')

def solution() :
    global K
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    result = 0

    while(K > 0) :
        for p in range(10, 0, -1):
            cells = active[p]
            new = []
            old = []
            if len(active[p]) > 0 :
                for ac in range(len(active[p])) :
                    y, x, hp = active[p][ac]
                    hp -= 1
                    if hp == -1 : # 세포배양
                        for d in range(4) :
                            ny = y + dy[d]
                            nx = x + dx[d]

                            if arr[ny][nx] == 0 :
                                arr[ny][nx] = p
                                new.append([ny, nx, p])
                        old.append(ac)
                    active[p][ac] = y, x, hp

                for _ in range(len(old)) :
                    active[p].pop(0)


                if len(new) :
                    active[p] += new
        K -= 1
    
    for i in range(1, 11):
        result += len(active[i])

    return result
                    





T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    in_arr = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0 for _ in range(700)] for _ in range(700)]
    active = list([] for _ in range(11))

    for i in range(N):
        for j in range(M) :
            arr[300+i][300+j] = in_arr[i][j]
            if in_arr[i][j] != 0 :
                active[in_arr[i][j]].append([300+i, 300+j, in_arr[i][j]])

    print('#{0} {1}'.format(t, solution()))

