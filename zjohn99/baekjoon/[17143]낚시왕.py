# baekjoon - [17143]낚시왕 (2020-10-18)
# https://www.acmicpc.net/problem/17143
import sys
sys.stdin = open("baekjoon/[17143]낚시왕.txt",'r')

def solution() :
    dy = []
    dx = []

T = int(input())
for t in range(1, T+1):
    R, C, M = map(int, input().split())
    mat = [[0 for in range(C)] for _ in range(R)]
    
    info = [list(map(int, input().split()) for _ in range(M))]
    # (r, c) // s 속력, d 이동방향, z 크기
    for i in range(len(info)) :
        mat[info[i][0]][info[i][1]] = 
    
    r, c, s, d, z = map(int, input().split())


