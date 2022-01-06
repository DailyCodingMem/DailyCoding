import math

def sosu(n):
    if n == 1 :
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

all_range = list(range(2, 246912))
memo = []

for i in all_range:
    if sosu(i):
        memo.append(i)

n = int(input())

while True:
    cnt = 0
    if n == 0 :
        break
    for i in memo:
        if n < i <= 2*n :
            cnt += 1
    print(cnt)
    n = int(input())
    