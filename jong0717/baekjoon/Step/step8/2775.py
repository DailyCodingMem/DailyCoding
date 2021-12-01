T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    zero_floor = [x for x in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            zero_floor[j] += zero_floor[j-1]
    print(zero_floor[-1])