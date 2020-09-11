import sys
sys.stdin = open("1216in.txt",'r')

for _ in range(10):
    Count = int(input())
    List  = list(input() for _ in range(100))
    Answer = 0
    for y in range(100):
        for x in range(100):
            for j in range(0,101-x):# 0 0~99 // 99, 
                String = List[y][x:x+j]
                if String == String[::-1] and len(String) > Answer:
                    Answer = len(String)
            
            String = ''
            for z in range(0,100-y):
                String += List[y+z][x]
                if String == String[::-1] and len(String) > Answer:
                    Answer = len(String)

    print("#{} {}".format(Count,Answer))