import math
N, S = map(int,input().split(' '))
bros = list(map(int,input().split(' ')))
ans = abs(S-bros[0])

if S == 1:
    print(ans)
else:
    for i in range(1,N):
        ans = math.gcd(ans, abs(S-bros[i]))
    print(ans)