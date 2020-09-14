T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = []
    cnt = 0
    for _ in range(8):
        arr.append(list(input()))
    for i in range(8):
        for j in range(8-n+1): # 5번 반복 # 0 1 2 3 4
            if arr[i][j:n+j] == list(reversed(arr[i][j:n+j])):
                cnt += 1

    for i in range(8): # 0 1 2 3 4 5 6 7
        for j in range(8-n+1): # 0 1 2 3 4
            temp = ''
            for p in range(n): # 0 1 2 3
                temp += arr[j+p][i]
            if list(temp) == list(reversed(temp)):
                cnt += 1

    print('#{} {}'.format(tc, cnt))