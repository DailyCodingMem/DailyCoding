import sys
sys.stdin = open("1449in.txt",'r')

n,l = map(int,sys.stdin.readline().split())
myList = sorted(list(map(int,sys.stdin.readline().split())), key=lambda x:x)
cnt = 0
answer = 0
while cnt<n:
    if cnt==0:
        start = myList[cnt]
        cnt += 1
        answer += 1
    else:
        if myList[cnt] in range(start,start+l):
            cnt += 1
        else:
            start = myList[cnt]
            answer += 1
print(answer)