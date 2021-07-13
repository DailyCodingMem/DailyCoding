n = int(input())
hansu_cnt = 0 
for i in range(1, n+1):
    hansu_list = list(map(int, str(i)))
    if i < 100:
        hansu_cnt += 1
    # n이 1000보다 작으니까 3자리 숫자여서 두개만 비교해보면 됨.
    elif hansu_list[0] - hansu_list[1] == hansu_list[1] - hansu_list[2]:
        hansu_cnt += 1

print(hansu_cnt)