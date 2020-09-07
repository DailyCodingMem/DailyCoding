# swea - [2005]파스칼의삼각형 (2020-09-07)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq

import sys
sys.stdin = open("swea/[2005]파스칼의삼각형.txt",'r')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    print("#{0}".format(t))
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if i == j :
                mat[i][j] = 1
            elif j == 0 :
                mat[i][j] = 1
            else :
                mat[i][j] = mat[i-1][j-1] + mat[i-1][j]
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                print(mat[i][j], end= " ")
        print()

    # 옛날에 내가 푼것
    # n = int(input())
    # tmp = []
    # tmp2 = []
    # for i in range(n):
    #     for j in range(i+1) :#012 / i 2
    #         if j == 0 or j == i :
    #             tmp2.append('1')
    #         else:
    #             tmp2.append(str(int(tmp[j]) + int(tmp[j-1])))
    #     tmp = tmp2[:]
    #     ans = ' '.join(tmp2)
    #     tmp2.clear()
    #     print(ans)