def clockwise(board):
    N = len(board)
    nboard = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            nboard[r][c] = board[N-c-1][r]
    return nboard
            
def solution(key, lock):
    def inchk(fr, fc):
        for r in range(fr, fr + N):
            for c in range(fc, fc + N):
                if board[r][c] + lock[r - fr][c - fc] != 1:
                    return False
        return True

    M = len(key)
    N = len(lock)
    line = M + 2 * N - 2
    board = [[0]*line for _ in range(line)]
    
    for r in range(N-1, N-1+M):
        for c in range(N-1, N-1+M):
            board[r][c] = key[r-N+1][c-N+1]
    # for _ in board:
    #     print(_)
    for dir in range(4):
        # for _ in lock:
        #     print(_)
        for fr in range(N + M - 1):
            for fc in range(N + M - 1):
                # print(fr, fc)
                if inchk(fr, fc):
                    return True
                # pass
        lock = clockwise(lock)
    return False