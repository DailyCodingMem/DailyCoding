#20200910
for tc in range(10):
    N = int(input())
    cnt = 0
    arr = [list(input()) for _ in range(8)]
    for i in range(8):
        for j in range(8-N+1):
            ans = ''
            for n in range(N):
                ans += arr[i][n+j]
            if ans == ans[::-1]:
                cnt += 1
    for j in range(8):
        for i in range(8-N+1):
            ans = ''
            for n in range(N):
                ans += arr[i+n][j]
            if ans == ans[::-1]:
                cnt += 1
    print(f'#{tc+1} {cnt}')
                
                