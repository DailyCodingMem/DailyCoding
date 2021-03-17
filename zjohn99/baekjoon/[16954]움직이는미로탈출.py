# baekjoon - [16954]움직이는미로탈출 (2021-01-20)
# https://www.acmicpc.net/problem/16954
import sys
from collections import deque
from pprint import pprint
sys.stdin = open("baekjoon/[16954]움직이는미로탈출.txt",'r')


def solution() :
    dy = [-1, -1, 0, 0, -1, 0] # 12시부터 시계방향 (7, 6, 5)제외
    dx = [0, 1, 1, -1, -1, 0]

    que = deque([(7,0,0,wall)])

    while(que) :
        y, x, day, walls = que.popleft()
        walls = moveWall(day, walls)
        if len(walls) == 0 :
            return 1
        if (y, x) in walls :
            continue

        for i in range(6) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 8 and 0 <= nx < 8 :
                if (ny, nx) not in walls :
                    que.append((ny, nx, day+1, walls))
    return 0





def moveWall(day, walls) :
    if day != 0 :
        tmp_wall = []
        for wy, wx in walls :
            wy += 1
            if wy < 8 :
                tmp_wall.append((wy, wx))
    else :
        return walls
    return tmp_wall



T = int(input())
for t in range(1, T+1):
    mat = [list(input()) for _ in range(8)]
    wall = []

    for i in range(8) :
        for j in range(8) :
            if mat[i][j] == '#' :
                wall.append((i,j))

    print(solution())


# def find():
#     stack = [(7, 0, 8)]  # 7, 0에서 시작. 땅높이 y==8
#     while stack:
#         y, x, ground = stack.pop()
#         for d in range(9): # 9방향
#             ny, nx = y + dy[d], x + dx[d]
#             if 0 <= ny < ground and 0 <= nx < 8 and MAP[ny][nx] == '.':  # 안전지대
#                 # 꼭대기층이면 성공
#                 if ny == 0:
#                     return 1
                
#                 # 미로를 내리는 대신 사람과 땅을 올림
#                 ny -= 1
#                 if MAP[ny][nx] == '.':  # 올린 칸도 안전지대
#                     # 꼭대기층이면 성공
#                     if ny == 0:
#                         return 1
#                     stack.append((ny, nx, ground - 1))  # 다음 탐색
#     return 0


# dx = (0, 0, 1, 1, 1, 0, -1, -1, -1)
# dy = (0, -1, -1, 0, 1, 1, 1, 0, -1)

# MAP = [input() for _ in range(8)]
# print(find())