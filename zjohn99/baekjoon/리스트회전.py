import sys
from pprint import pprint
sys.stdin = open("baekjoon/리스트회전.txt",'r')

def zip_rotate(original) :
    # rotated = zip(*original[::-1])
    # return [list(rot) for rot in rotated]
    rotated = list(map(list, zip(*original[::-1])))
    return rotated
def rotate(original) :   
    n = len(original)
    m = len(original[0])
    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = mat[i][j]

    return 0
    
T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    pprint(mat)
    pprint(zip_rotate(mat))

