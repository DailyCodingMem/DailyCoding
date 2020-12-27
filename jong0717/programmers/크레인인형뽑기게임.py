def solution(board, moves):
    basket = []
    answer = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] > 0 :
                basket.append(board[i][j-1])
                board[i][j-1] = 0
                if basket[-1:] == basket[-2:-1]:
                    answer += basket[-1:]
                    basket = basket[:-2]
                break
    return len(answer)*2

