import sys
sys.stdin = open("1764in.txt",'r')

N,M = map(int,input().split())
NoListen = set()
NoSee = set()
for _ in range(N):
    NoListen.add(input())
for _ in range(M):
    NoSee.add(input())
result = list(NoListen&NoSee)
print(len(result))
for e in sorted(result): 
    print(e)