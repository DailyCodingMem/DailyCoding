import sys
sys.stdin = open("in.txt",'r')

N = int(input())
STACK = []
for i in range(N):
    Str = input()
    if Str[:3]=="pus":
        String = Str.split()
        # print(String)
        STACK.append(int(String[1]))
    elif Str[:3]=="top":
        if STACK:
            print(STACK[-1])
        else:
            print(-1)
    elif Str[:3]=="pop":
        if STACK:
            STACK.pop()
        
    elif Str[:3]=="siz":
        print(len(STACK))
    elif Str[:3]=="emp":
        if STACK:
            print("false")
        else:
            print("true")