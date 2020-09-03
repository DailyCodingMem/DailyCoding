year = int(input())

if year % 4 == 0 and year % 100:
    print('yes')
elif year % 400 == 0:
    print('yes')
else:
    print('no')