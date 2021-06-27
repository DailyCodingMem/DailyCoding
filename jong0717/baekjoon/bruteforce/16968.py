car_num = input()
ans = 1
if car_num:
    ans = 26 if car_num[0] == 'c' else 10
    for i in range(1,len(car_num)):
        if car_num[i] == 'c':
            if car_num[i-1] == 'c':
                ans *= 25
            else:
                ans *= 26
        else:
            if car_num[i-1] == 'd':
                ans *= 9
            else:
                ans *= 10
print(ans)