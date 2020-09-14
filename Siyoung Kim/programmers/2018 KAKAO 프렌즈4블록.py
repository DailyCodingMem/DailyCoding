def printB(board):
    for line in board:
        print(line)

def fall(board):
    for c in range(len(board[0])):
        stack = []
        for r in range(len(board)):
            if board[r][c]:
                stack.append(board[r][c])
                board[r][c] = ''
        for r in range(len(board)-1, -1, -1):
            if not stack:
                break
            board[r][c] = stack.pop()
                
def solution(m, n, board):
    answer = 0 
    
    for index, line in enumerate(board):
        board[index] = list(line)
        
    delboard = [[0] * n for _ in range(m)]
    
    while True:
        delflag = False
        
        for r in range(m-1):
            for c in range(n-1):
                if board[r][c] and board[r][c] == board[r][c+1] == board[r+1][c] == board[r+1][c+1]:
                    delboard[r][c] = delboard[r][c+1] = delboard[r+1][c] = delboard[r+1][c+1] = 1
                    delflag = True
                    
        if not delflag:
            break
            
        for r in range(m):
            for c in range(n):
                if delboard[r][c]:
                    delflag = True
                    board[r][c] = ''
                    delboard[r][c] = 0
                    answer += 1
        fall(board)
        # printB(board)
        # break
                    
    return answer