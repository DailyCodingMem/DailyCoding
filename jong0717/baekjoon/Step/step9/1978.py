N = int(input())
numbers = map(int,input().split())
cnt = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2,num):
            if num % i == 0:
                error += 1
        if error == 0:
            cnt += 1
# print(cnt)
print('a=', 20, 'b=', 2)