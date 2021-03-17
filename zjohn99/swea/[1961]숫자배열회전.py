# swea - [1961]숫자배열회전 (2020-10-18)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE

import sys
sys.stdin = open("swea/[1961]숫자배열회전.txt",'r')

# 시계 방향으로 90 / 180 / 270
# 규칙은 [행][열]  ->  [열][ab(행-크기)]

def solution() :
    nMat = [['' for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            val = abs(i-N+1)
            nMat[j][val] = mat[i][j]
            # newArr[j][N-1-i] = arr[i][j]
    return nMat

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(str, input().split())) for _ in range(N)]
    result = [['' for _ in range(3)] for _ in range(N)]
    
    for i in range(3) :
        mat = solution()
        
        for j in range(N) :
            result[j][i] = ''.join(mat[j])
    print('#{0}'.format(t))
    for i in range(N) :
        for j in range(3) :
            print(result[i][j], end=' ')
        print()
    
