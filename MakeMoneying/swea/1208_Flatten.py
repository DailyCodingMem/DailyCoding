import sys
sys.stdin = open("1208in.txt",'r')

for Count in range(10):
    N = int(input())
    List = list(map(int,input().split()))
    for _ in range(N):
        Max = max(List)
        MaxIndex = List.index(Max)
        Min = min(List)
        MinIndex = List.index(Min)
        List[MaxIndex] -= 1
        List[MinIndex] += 1
    Max = max(List)
    Min = min(List)
    print("#{} {}".format(Count+1,Max-Min))