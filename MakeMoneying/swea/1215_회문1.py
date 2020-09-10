import sys
sys.stdin = open("1215in.txt",'r')
for Count in range(10):
    N = int(input())
    List = list(input() for _ in range(8))
    Answer = 0
    
    # 가로 확인
    for y in range(8):
        for x in range(8-N+1):
            A = List[y][x:x+N]
            if A == A[::-1]:
                Answer += 1

    # 세로 확인
    for y in range(8-N+1):
        for x in range(8):
            A = ''
            for z in range(N):
                A += List[y+z][x]
            if A == A[::-1]:
                Answer += 1    
    print("#{} {}".format(Count+1,Answer))