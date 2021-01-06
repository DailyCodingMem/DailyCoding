import sys
sys.stdin = open("1946in.txt",'r')


for count in range(int(input())):
    N = int(input())
    List = list( 0 for _ in range(N+1))
    for _ in range(N):
        A,B = map(int,input().split())
        List[A] = B
    MinScore = List[1]
    cnt = 0
    for i in range(2,len(List)):
        if MinScore > List[i]:
            MinScore = List[i]
        else:
            cnt += 1
    print(N-cnt)