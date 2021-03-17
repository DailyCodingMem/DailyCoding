import sys
sys.stdin = open("13458in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
a,b = map(int,sys.stdin.readline().split())
ans = 0
for s in li:
    ans += 1
    if (s-a)>0:
        if (s-a)%b:
            ans += ((s-a)//b +1)
        else:
            ans += (s-a)//b
print(ans)