import sys
sys.stdin = open("1164in.txt",'r')

A,B,C = map(int,input().split())
if A <=170 or B<=170 or C<=170:
    print("CRASH")
else:
    print("PASS")