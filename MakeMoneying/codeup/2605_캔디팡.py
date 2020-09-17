List = [list(map(int,input().split())) for _ in range(7)]
# List = [[2, 1, 5, 1, 1, 3, 4], [2, 1, 5, 1, 3, 5, 3], [2, 3, 4, 5, 2, 2, 4], [4, 4, 3, 2, 3, 1, 3], [4, 3, 5, 3, 1, 4, 3], [5, 4, 4, 3, 3, 5, 5], [2, 1, 3, 5, 1, 1, 2]]

check_list = [[True for _ in range(7)] for _ in range(7) ] # True가 아직 안본 애들

# 왼 오 위 아래
dy = [0,0,-1,1]
dx = [-1,1,0,0]

def candy(A,y,x):
    global Basket,check_list
    for i in range(4):
        Y = y+dy[i]
        X = x+dx[i]
        if 0<=Y<7 and 0<=X<7 and check_list[Y][X]: # 벽 판별, 체크 안봤는지 확인
            if A==List[Y][X]:
                Basket.append((Y,X))
                check_list[Y][X]=False # 한 번 봣으면 체크
                candy(A,Y,X)


answer = 0
for y in range(7):
    for x in range(7):
        if check_list[y][x] : # True 일때만 실행
            A = List[y][x] # 이 때의 색깔을 A
            check_list[y][x] = False # 한 번 봣으면 False
            Basket = [(y,x)]
            candy(A,y,x)
            if len(Basket)>=3: # 만약 그게 3개 이상이라면
                answer += 1
print(answer)





