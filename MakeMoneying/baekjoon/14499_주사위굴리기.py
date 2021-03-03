import sys
sys.stdin = open("14499in.txt",'r')

import sys
dice = list(([0]*3 for _ in range(4)))
n,m,y,x,k = map(int,sys.stdin.readline().split())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
basket = list(map(int,sys.stdin.readline().split()))
for i in basket:
    if i==1 and x+1<m:
        x += 1
        a = dice[1][0]
        dice[1][0] = dice[1][1]
        if li[y][x]:
            dice[1][1] = li[y][x]
            li[y][x] = 0
     
        else:
            dice[1][1] = dice[1][2]
            li[y][x] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = a
        print(a)
    elif i == 2 and x>0:
        x -= 1
        a = dice[1][2]
        dice[1][2] = dice[1][1]
        if li[y][x]:
            dice[1][1] = li[y][x]
            li[y][x] = 0
        else:
            dice[1][1] = dice[1][0]
            li[y][x] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = a
        print(a)
    elif i == 3 and y>0:
        y -= 1
        a = dice[2][1]
        dice[2][1] = dice[1][1]
        if li[y][x]:
            dice[1][1] = li[y][x]
            li[y][x] = 0
        else:
            dice[1][1] = dice[0][1]
            li[y][x] = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = a
        print(a)
    elif i == 4 and y+1<n:
        y += 1
        a = dice[0][1]
        dice[0][1] = dice[1][1]
        if li[y][x]:
            dice[1][1] = li[y][x]
            li[y][x] = 0
        else:
            dice[1][1] = dice[2][1]
            li[y][x] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = a
        print(a)