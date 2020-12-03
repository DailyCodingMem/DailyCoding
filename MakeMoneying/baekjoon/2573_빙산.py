import sys
sys.stdin = open("2573in.txt",'r')



import sys
sys.setrecursionlimit(10**6)

Y,X = map(int,input().split())
List = list(list(map(int,input().split())) for _ in range(Y))

# 위 아래 왼쪽 오른쪽
dy = [-1,1,0,0]
dx = [0,0,-1,1]
result = 0

def bingSan(y,x):
    global basket, visited

    checkBasket = [(y,x)]

    while checkBasket:
        y,x = checkBasket.pop(0)
        basket.append((y,x))
        cnt = 0
        for j in range(4):
            cntY = y + dy[j]
            cntX = x + dx[j]
            if 0<=cntY<Y and 0 <= cntX < X and not List[cntY][cntX]:
                cnt += 1
        basket.append(cnt)
        for i in range(4):
            newY = y + dy[i]
            newX = x + dx[i]
            if 0<= newY < Y and 0 <= newX < X and visited[newY][newX] and List[newY][newX]:
                checkBasket.append((newY,newX))
                visited[newY][newX] = False

        

 
year = 0
while True:
    result = 0
    no = 0
    visited = list( list( True for _ in range(X)) for _ in range(Y) )
    # 한번은 걸려라
    for y in range(Y):
        for x in range(X):
            if List[y][x] and visited[y][x]: # 걸렸다.
                no += 1
                if no > 1:
                    break
                visited[y][x] = False
                basket = []
                bingSan(y,x)

            elif not List[y][x]:
                result += 1
            
        if no > 1:
            break
    year += 1
    if no == 1:
        for _ in range(len(basket)//2):
            water = basket.pop()
            locY, locX = basket.pop()
            List[locY][locX] = max(0,List[locY][locX]-water)
        pass
    elif no == Y*X:
        print(0)
        break
    elif no > 1:
        print(year-1)
        break