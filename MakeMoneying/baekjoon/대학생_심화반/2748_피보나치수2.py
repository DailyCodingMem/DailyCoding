import sys
sys.stdin = open("2748in.txt",'r')

import sys
n = int(sys.stdin.readline())

ba = {}
ba[0] = 0
ba[1] = 1
for i in range(2,n+1):
    ba[i] = ba[i-2]+ba[i-1]
print(ba[n])