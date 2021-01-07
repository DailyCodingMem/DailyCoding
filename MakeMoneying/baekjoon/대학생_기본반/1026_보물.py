import sys
sys.stdin = open("1026in.txt",'r')

N = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
a.sort()
answer = 0
for i in range(N):
    Max = 0
    for j in range(N):
        if Max <= b[j]:
            Max = b[j]
            k = j
    answer += a[i]*b[k]
    b[k] = 0
print(answer)