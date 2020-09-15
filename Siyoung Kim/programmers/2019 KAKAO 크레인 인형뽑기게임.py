board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def printB(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print()


from collections import deque


def solution(board, moves):
    printB(board)
    stack = deque()

    score = 0

    tops = [0] * len(board)
    for c in range(len(board)):
        for r in range(len(board)):
            if board[r][c]:
                tops[c] = r
                break
        else:
            tops[c] = len(board)

    for col in moves:
        h = tops[col-1]
        if h >= len(board):
            continue
        now = board[h][col-1]
        board[h][col-1] = 0
        tops[col-1] += 1
        if stack and now == stack[-1]:
            stack.pop()
            score += 2
        else:
            stack.append(now)
        # print(col)
        # print(stack)
        # printB(board)


    return score


print(solution(board, moves))