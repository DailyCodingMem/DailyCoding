import sys
sys.stdin = open("10828in.txt",'r')

import sys
n = int(sys.stdin.readline())
ba = []
for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[-1].isdigit():
        a,b = a.split()

    if a =="push":
        ba.append(b)
    elif a == "pop":
        if ba:
            print(ba.pop())
        else:
            print(-1)
    elif a == "size":
        print(len(ba))
    elif a =="empty":
        if ba:
            print(0)
        else:
            print(1)
    elif a == "top":
        if ba:
            print(ba[-1])
        else:
            print(-1)