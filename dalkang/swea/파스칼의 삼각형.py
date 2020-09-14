T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [[0 for _ in range(n*2-1)] for _ in range(n)]
    arr[0][(n*2-1)//2] = 1
 
    for i in range(1, n):
        for j in range(n*2):
            if j-1 < 0:
                j=0
                arr[i][j] = arr[i-1][j+1]
            elif j+1 > 2*n-2:
                j=2*n-2
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
    print('#{} '.format(t))
    for i in range(n):
        for j in range(2*n-1):
            if arr[i][j] > 0:
                print(arr[i][j], end =' ')
        print()