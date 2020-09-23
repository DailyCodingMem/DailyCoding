from copy import deepcopy

board = [
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    # [0][4]에 멈출 경우
    [13, 16, 19, 25, 30, 35, 40],
    # [0][9]에 멈출 경우
    [22, 24, 25, 30, 35, 40],
    # [0][14]에 스탑
    [28, 27, 26, 25, 30, 35, 40]
]
branch = {
    (0, 4): (1, -1),
    (0, 9): (2, -1),
    (0, 14): (3, -1)
}
change = {
    (1, 6): (0, 19),
    (2, 2): (1, 3),
    (2, 3): (1, 4),
    (2, 4): (1, 5),
    (2, 5): (0, 19),
    (3, 3): (1, 3),
    (3, 4): (1, 4),
    (3, 5): (1, 5),
    (3, 6): (0, 19)
}


def permutations(current, deban, score, location, end, start):
    def move(koma, deban):
        r, c = nlocation[koma]
        distance = dice[deban]
        nc = c + distance
        if nc >= len(board[r]):
            nlocation[koma] = (-1, -1)
            return -1
        add = board[r][nc]
        if (r, nc) in branch:
            r, nc = branch[r, nc]
        if (r, nc) in change:
            r, nc = change[r, nc]
        if (r, nc) in nlocation:
            return False
        nlocation[koma] = (r, nc)
        return add

    # print(current,score,location)

    # print(score)
    global maxScore
    if maxScore < score:
        maxScore = score
        # print(score)
    if len(current) == 10:
        return

    for i in range(min(4, start + 1)):
        if i in end:
            continue
        nlocation = deepcopy(location)
        add = move(i, deban)
        # print(add)
        if not add:
            continue
        nscore = score
        nend = end[:]
        if add == -1:
            nend.append(i)
        else:
            nscore = score + add
        ncurrent = current[:]
        ncurrent.append(i)
        permutations(ncurrent, deban + 1, nscore, nlocation, nend, max(start + 1, i + 1))


maxScore = -1
location = [(0, -1)] * 4
dice = list(map(int, input().split()))
end = []
permutations([], 0, 0, location, end, 0)
print(maxScore)