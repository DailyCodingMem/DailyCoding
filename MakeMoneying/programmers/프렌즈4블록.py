def bbang(List,ay,ax,visited):
    if 0<=ay+1<len(List) and 0<=ax+1<len(List[0]) and List[ay][ax] == List[ay+1][ax] == List[ay][ax+1] == List[ay+1][ax+1]:
        visited[ay][ax] = False
        visited[ay][ax+1] = False
        visited[ay+1][ax+1] = False
        visited[ay+1][ax] = False
    elif not List[ay][ax]:
        visited[ay][ax] = False

                

def solution(Y, X, board):
    List = []
    last = 0
    for i in board:
        boardList = []
        for j in i:
            boardList.append(j)
        List.append(boardList)
    # 무한 루프
    while True:
        visited = [[True for _ in range(X)] for _ in range(Y)]
        # 4개씩 짝 맞추기
        for y in range(Y-1):
            for x in range(X-1):
                bbang(List,y,x,visited)
        answer = 0
        for y in range(Y):
            for x in range(X):
                if not visited[y][x]:
                    List[y][x] = 0
                    answer += 1
        # 결과가 달라지지 않았으면 출력
        if last == answer:
            return answer

        # 내리는 작업
        else:
            last = answer
            for y in range(Y-1,-1,-1):
                for x in range(X-1,-1,-1):
                    if not List[y][x]: # 0일 때
                        cnt = 1
                        while 0<= (y-cnt) and not List[y-cnt][x]:
                            cnt += 1
                        if 0<=(y-cnt):
                            List[y][x] = List[y-cnt][x]
                            List[y-cnt][x] = 0


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m,n,board)) # m이 Y
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(4 , 5, ["AAAAA","AUUUA","AUUAA","AAAAA"] ))
print(solution(3 , 3, ["AAA","AAA","AAB"]))