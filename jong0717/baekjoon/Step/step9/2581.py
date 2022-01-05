M = int(input())
N = int(input())
sosu_sum = []
for num in range(M, N+1):
    error = 0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            sosu_sum.append(num)
if len(sosu_sum) > 0:
    print(sum(sosu_sum))
    print(min(sosu_sum))
else:
    print(-1)