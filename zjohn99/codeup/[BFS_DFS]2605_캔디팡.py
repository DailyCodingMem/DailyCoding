# codeup - BFS/DFS - 캔디팡 (2020-09-14)
# https://codeup.kr/problem.php?id=1380

import sys
sys.stdin = open("codeup/[BFS_DFS]2605_캔디팡.txt",'r')

def solution():
    dy = [-1,0,1,0] # 12시부터 시계방향
    dx = [0,1,0,-1]
    
    count = 0 # 눌렀을때, 터지는 영역의 갯수 

    for p in range(7): 
        for q in range(7):
            if check[p][q] == False :

                syn = 1 # 몇개가 연속으로 이어져 있는지 갯수를 알기 위해
                check[p][q] = True
                color = mat[p][q] # 해당 색상값
                st = [(p,q)]

                while(st) :
                    y,x = st[-1]
                    for i in range(4):
                        ny = dy[i] + y        
                        nx = dx[i] + x

                        if ny >= 0 and ny < 7 and nx >= 0 and nx < 7 : # mat안에 존재할 때, 벽꿍x
                            if color == mat[ny][nx] and check[ny][nx] == False:
                                st.append((ny,nx))
                                check[ny][nx] = True
                                syn += 1
                                break
                    else :
                        st.pop(-1)
                if syn >= 3 : # 연속 3개 이상일 때, 터친다.
                    count += 1
    return count
        
                            


    


T = int(input())
for _ in range(T):
    mat = [list(map(int, input().split())) for _ in range(7)]
    check = [[False for _ in range(7)] for _ in range(7)]
    
    print(solution())
