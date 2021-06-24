def solution(m, n, board):
    answer = 0
    # board를 사용하기 편하게 2차원 배열로 만들기.
    for i in range(len(board)):
        board[i] = list(board[i])
    while True:
        # 2x2 찾으면 remove 배열에 1로 표시하기
        remove = [[0]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    remove[i][j], remove[i+1][j], remove[i][j+1], remove[i+1][j+1] = 1, 1, 1, 1

        count = 0
        # count에 remove에 있는 1의 합을 더해주면서 지운 갯수 누적
        for i in range(m):
            count += sum(remove[i])
        # answer에 누적
        answer += count
        # count가 0이라는건 더이상 2x2가 없다는 이야기이므로 탈출!
        if count == 0:
            break
        # 지워진 블록을 다른 블록으로 채우기
        # 아래서부터 접근해서 위로 올라가면서
        for i in range(m-1, -1, -1):
            for j in range(n):
                # 1이면 x를 감소시켜나가면서 접근
                if remove[i][j] == 1:
                    x = i - 1
                    # remove가 1이면 계속 위로 올라가야함으로 while로 반복
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1
                    # 음수가 나오면 더이상 문자가 없는거니까 0저장
                    if x < 0 :
                        board[i][j] = 0
                    # i,j의 문자를 x,j로 할당하면 위의 문자가 아래로 내려온거로 됨 
                    else:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1
    return answer

