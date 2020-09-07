#20200907
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)]for _ in range(N)]
    arr[0][0] = 1
    # 0부터 하면 다시 arr[0][0]이 0이 되어 그냥 다 0이되버림
    for i in range(1,N):
        for j in range(N):
            #2차원도 -인덱스로 접근가능! arr[0][3] = arr[0][-1] -인덱스들에 접근되었을때
            # 해당값들이 0으로 할당되어있어서 원하는 계산이 가능
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = ''
    print(f'#{tc+1}')
    for i in arr:
        print(*i)




# 예전에 푼거
# def factorial(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# def answer(n):
#     for i in range(n):
#         n_com = int(factorial(n-1) / (factorial(i)*factorial(n-1-i)))
#         print(n_com, end=' ')
#     print()

# T = int(input())
# for t in range(T):
#     n = int(input())
#     print('#{}'.format(t+1))
#     for i in range(1,n+1):
#         answer(i)