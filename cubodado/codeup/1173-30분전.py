hour, minute = map(int, input().split())

if minute < 30:
    if hour == 0:
        print(23, )
    else:
        print(hour-1, abs(minute-30))
else:
    print(hour, minute-30)