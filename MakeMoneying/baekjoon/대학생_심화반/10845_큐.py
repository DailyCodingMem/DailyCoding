import sys
sys.stdin = open("10845in.txt",'r')

import sys
from collections import deque
n = int(sys.stdin.readline())
ba = deque([])
for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[-1].isdigit():
        a,b = a.split()
        b = int(b)
    if a=="push":
        ba.append(b)
    elif a=="pop":
        if ba:
            print(ba.popleft())
        else:
            print(-1)
    elif a=="size":
        print(len(ba))
    elif a=="empty":
        if ba:
            print(0)
        else:
            print(1)
    elif a=="front":
        if ba:
            print(ba[0])
        else:
            print(-1)
    elif a=="back":
        if ba:
            print(ba[-1])
        else:
            print(-1)
