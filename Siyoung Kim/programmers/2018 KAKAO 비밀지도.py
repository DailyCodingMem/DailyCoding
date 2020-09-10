def solution(n, arr1, arr2):
    board = [''] * n
    for i in range(n):
        for v in bin(arr1[i] | arr2[i])[2:].zfill(n):
            if v == '1':
                board[i] += '#'
            else:
                board[i] += ' '
    return board