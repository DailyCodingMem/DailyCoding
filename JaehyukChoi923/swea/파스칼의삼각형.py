T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    arr[0][0] = 1
    for i in range(1, n): # 1 2 3
        for j in range(n): # 0 1 2 3
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print('#{}'.format(tc))
    for i in arr:
        for j in i:
            if j != 0:
                print(j, end=' ')
        print()
