# baekjoon - [12100]2048 (2021-02-24)
# https://www.acmicpc.net/problem/12100

from sys import stdin
from copy import deepcopy
import itertools
stdin = open("baekjoon/[12100]2048.txt",'r')

def solution(dir) :
    tmp_mat = [[0 for _ in range(N)] for _ in range(N)]

    if dir == 0 : # 상
        for i in range(N) :
            check = True # 첫칸이거나 한번이라도 더하지 않았을경우 true
            lv = 0
            for j in range(N) :
                if mat[j][i] != 0 :
                    tmp_val = mat[j][i]
                    if check : # 첫 칸 or 더해진 다음 값
                        tmp_mat[lv][i] = mat[j][i]
                        lv += 1
                        check = False
                    else : # 첫 칸 이후
                        if tmp_mat[lv-1][i] != tmp_val : # 이전의 값과 다를때
                            tmp_mat[lv][i] = mat[j][i]
                            lv += 1
                        else : # 값이 같았을 경우
                            tmp_mat[lv-1][i] += mat[j][i]
                            check = True

    elif dir == 1 : # 우
        for i in range(N-1, -1, -1) :
            check = True 
            lv = N-1
            for j in range(N-1, -1, -1) :
                if mat[i][j] != 0 :
                    tmp_val = mat[i][j]
                    if check :
                        tmp_mat[i][lv] = mat[i][j]
                        lv -= 1
                        check = False
                    else : 
                        if tmp_mat[i][lv+1] != tmp_val :
                            tmp_mat[i][lv] = mat[i][j]
                            lv -= 1
                        else : 
                            tmp_mat[i][lv+1] += mat[i][j]
                            check = True
    elif dir == 2 : # 하
        for i in range(N-1, -1, -1) :
            check = True 
            lv = N-1
            for j in range(N-1, -1, -1) :
                if mat[j][i] != 0 :
                    tmp_val = mat[j][i]
                    if check :
                        tmp_mat[lv][i] = mat[j][i]
                        lv -= 1
                        check = False
                    else : 
                        if tmp_mat[lv+1][i] != tmp_val :
                            tmp_mat[lv][i] = mat[j][i]
                            lv -= 1
                        else : 
                            tmp_mat[lv+1][i] += mat[j][i]
                            check = True
    else : # 좌
        for i in range(N) :
            check = True 
            lv = 0
            for j in range(N) :
                if mat[i][j] != 0 :
                    tmp_val = mat[i][j]
                    if check :
                        tmp_mat[i][lv] = mat[i][j]
                        lv += 1
                        check = False
                    else : 
                        if tmp_mat[i][lv-1] != tmp_val :
                            tmp_mat[i][lv] = mat[i][j]
                            lv += 1
                        else : 
                            tmp_mat[i][lv-1] += mat[i][j]
                            check = True
    
    return tmp_mat



T = int(stdin.readline())
for t in range(1, T+1) :
    N = int(stdin.readline())
    mat = [list(map(int, stdin.readline().split())) for _ in range(N)]
    bat = deepcopy(mat)
    arr = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
    a = itertools.permutations(arr,5)
    a = set(a)
    max_val = 0
    for i in a :
        for j in i :
            mat = deepcopy(solution(j))
        for p in range(N):
            for q in range(N) :
                if max_val <= mat[p][q] :
                    max_val = mat[p][q]
        mat = deepcopy(bat)
        
    print(max_val)
