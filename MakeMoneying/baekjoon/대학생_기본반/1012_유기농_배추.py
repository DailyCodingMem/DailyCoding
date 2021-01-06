import sys
sys.stdin = open("1012in.txt",'r')

from collections import deque
T = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for count in range(T):
    M,N,K = map(int,input().split())
    List = list(list(0 for _ in range(M)) for _ in range(N))
    for _ in range(K):
        A,B = map(int,input().split())
        List[B][A] = 1
    
    answer = 0
    for y in range(N):
        for x in range(M):
            if List[y][x]:
                answer += 1
                basket = deque([(y,x)])
                visited = list(list(True for _ in range(M)) for _ in range(N))
                visited[y][x] = False
                while basket:
                    newY,newX = basket.popleft()
                    for i in range(4):
                        checkY = newY + dy[i]
                        checkX = newX + dx[i]
                        if 0<= checkY < N and 0 <= checkX < M and visited[checkY][checkX] and List[checkY][checkX]:
                            visited[checkY][checkX] = False
                            List[checkY][checkX] = 0
                            basket.append((checkY,checkX))
    print(answer)