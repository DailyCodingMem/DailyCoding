import sys
sys.stdin = open("1209in.txt",'r')

for _ in range(10):
    Count = int(input())
    List = [list(map(int,input().split())) for _ in range(100)]
    Max = 0
    for y in range(100):
        Answer1 = Answer2 = Answer3 = 0
        for x in range(100):
            Answer1 += List[y][x]
            Answer2 += List[x][y]
            Answer3 += List[x][x]
        Max = max(Answer1,Answer2,Max)
    print("#{} {}".format(Count,Max))

        