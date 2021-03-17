import sys
sys.stdin = open("2583in.txt",'r')

M,N,K = map(int,input().split())
List = list(list( 1 for _ in range(N)) for _ in range(M))
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    maxY = max(y2,y1)
    minY = min(y2,y1)
    maxX = max(x2,x1)
    minX = min(x2,x1)
    for y in range(minY,maxY):
        for x in range(minX,maxX):
            List[y][x] = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
answer = []
for y in range(M):
    for x in range(N):
        if List[y][x]:
            cnt = 1
            basket = [(y,x)]
            List[y][x] = 0
            while basket:
                newY,newX = basket.pop()
                for i in range(4):
                    checkY = newY + dy[i]
                    checkX = newX + dx[i]
                    if 0 <= checkY < M and 0 <= checkX < N and List[checkY][checkX]:
                        cnt += 1
                        List[checkY][checkX] = 0
                        basket.append((checkY,checkX))
            answer.append(cnt)
answer.sort()
print(len(answer))
print(*answer)