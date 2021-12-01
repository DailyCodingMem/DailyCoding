T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    cnt = 0
    distance = y - x
    move = 1
    move_sum = 0
    while move_sum < distance:
        cnt += 1
        move_sum += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)