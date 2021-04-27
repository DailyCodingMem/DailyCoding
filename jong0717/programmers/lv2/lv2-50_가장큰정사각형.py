def solution(board):
    answer = 0
    # DP 이용, 대각, 좌, 위 값중에 최솟값을 더해줌으로 가능한 한변의 길이를 저장
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
    for i in range(len(board)):
        tmp = max(board[i])
        answer = max(answer, tmp)
    return answer**2
