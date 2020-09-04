number = int(input())
check = 0

for n in range(2, number+1):
    if number % n == 0:
        check += 1
if check == 1:
    print('prime')
else:
    print('not prime')