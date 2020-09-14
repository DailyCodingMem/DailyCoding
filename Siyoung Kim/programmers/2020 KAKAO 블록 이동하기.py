from collections import deque

delta = (
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
)


def solution(board):
    N = len(board)

    garo_visit = [[0] * N for _ in range(N)]
    sero_visit = [[0] * N for _ in range(N)]

    q = deque()
    sr = 0
    sc = 0
    q.append((sr, sc, True, 0))
    garo_visit[sr][sc] = 1
    while q:
        # print(q)
        row, col, isgaro, time = q.popleft()
        if (isgaro and row == N - 1 and col == N - 2) or (not isgaro and row == N - 2 and col == N - 1):
            return time

        # 상하좌우이동
        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if isgaro:
                if 0 <= nr < N and 0 <= nc < N - 1 and board[nr][nc] == 0 and board[nr][nc + 1] == 0:
                    # if nr == N - 1 and nc == N - 2:
                    #     return time + 1
                    if garo_visit[nr][nc] == 0:
                        garo_visit[nr][nc] = 1
                        q.append((nr, nc, True, time + 1))
            else:
                if 0 <= nr < N - 1 and 0 <= nc < N and board[nr][nc] == 0 and board[nr + 1][nc] == 0:
                    # if nr == N - 2 and nc == N - 1:
                    #     return time + 1
                    if sero_visit[nr][nc] == 0:
                        sero_visit[nr][nc] = 1
                        q.append((nr, nc, False, time + 1))
        # 회전
        # 기준점 축
        if isgaro:
            # 가로 아래쪽
            if row + 1 < N and col + 1 < N and board[row + 1][col] == 0 and board[row + 1][col + 1] == 0:
                if not sero_visit[row][col]:
                    sero_visit[row][col] = 1
                    q.append((row, col, False, time + 1))
                if not sero_visit[row][col + 1]:
                    sero_visit[row][col + 1] = 1
                    q.append((row, col + 1, False, time + 1))
            # 가로 위쪽
            if row - 1 >= 0 and col + 1 < N and board[row - 1][col] == 0 and board[row - 1][col + 1] == 0:
                if not sero_visit[row - 1][col]:
                    sero_visit[row - 1][col] = 1
                    q.append((row - 1, col, False, time + 1))
                if not sero_visit[row - 1][col + 1]:
                    sero_visit[row - 1][col + 1] = 1
                    q.append((row - 1, col + 1, False, time + 1))
        else:
            if row + 1 < N and col + 1 < N and board[row][col + 1] == 0 and board[row + 1][col + 1] == 0:
                if not garo_visit[row][col]:
                    garo_visit[row][col] = 1
                    q.append((row, col, True, time + 1))
                if not garo_visit[row + 1][col]:
                    garo_visit[row + 1][col] = 1
                    q.append((row + 1, col, True, time + 1))
            if row + 1 < N and col - 1 >= 0 and board[row][col - 1] == 0 and board[row + 1][col - 1] == 0:
                if not garo_visit[row][col - 1]:
                    garo_visit[row][col - 1] = 1
                    q.append((row, col - 1, True, time + 1))
                if not garo_visit[row + 1][col - 1]:
                    garo_visit[row + 1][col - 1] = 1
                    q.append((row + 1, col - 1, True, time + 1))

    return -1