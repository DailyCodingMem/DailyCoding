import sys
sys.stdin = open("2805in.txt",'r')
import sys
N,M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
l ,r = 1,1000000000
while l <= r:
    m = (l+r)//2
    c = 0
    for i in trees:
         c+=(i-m) if i>m else 0
    if c >= M: l = m+1
    else: r = m-1
print(r)