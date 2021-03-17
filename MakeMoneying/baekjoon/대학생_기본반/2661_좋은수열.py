import sys
sys.stdin = open("2661in.txt",'r')

def back_tracking(cnt):

    for i in range(1,cnt//2+1):
        if s[-2*i:-i] == s[-i:]:
            return False

    if cnt==n:
        for k in s:
            print(k, end='')
        return True

    for j in range(1,4):
        s.append(j)
        if back_tracking(cnt+1):
            return True
        s.pop()

n = int(input())
s = []
back_tracking(0)