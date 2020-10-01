#20200909
N = int(input())
for i in range(N // 2, -1, -1):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, (N - i * 2)):
        print('*', end='')
    for j in range(0, i):
        print(' ', end='')
    print()