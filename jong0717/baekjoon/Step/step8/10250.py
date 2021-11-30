T = int(input())
for t in range(T):
    H, W, N = map(int,input().split())
    one = (N // H) + 1
    floor = N % H
    if floor == 0:
        one = N // H
        floor = H
    print(f'{floor * 100 + one}')
