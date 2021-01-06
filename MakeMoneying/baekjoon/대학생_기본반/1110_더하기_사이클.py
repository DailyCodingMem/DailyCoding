import sys
sys.stdin = open("1110in.txt",'r')

def changeNumber(N):
    if N<10:
        return N*11
    else:
        a = N%10 + N//10
        if a>=10:
            b = a%10
        else:
            b = a
        c = N%10
        return c*10 + b

def findCycle(N):
    cnt = 0
    check = N
    while True:
        check = changeNumber(check)
        cnt += 1
        if check == N:
            return cnt
N = int(input())
print(findCycle(N))