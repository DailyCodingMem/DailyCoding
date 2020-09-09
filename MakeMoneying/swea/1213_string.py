import sys
sys.stdin = open("1213in.txt",'r',encoding='utf-8')

for _ in range(10):
    Count = int(input())
    Check = input()
    String = input()
    Answer = 0
    for i in range(0,len(String)-len(Check)+1):
        if String[i] == Check[0]:
            for j in range(len(Check)+1):
                if j==len(Check):
                    Answer += 1
                else:
                    if String[i+j] != Check[j]:
                        break
    print("{} {}".format(Count,Answer))