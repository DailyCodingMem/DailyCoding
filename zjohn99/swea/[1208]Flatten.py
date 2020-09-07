# swea - [1206]view (2020-09-07)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh

import sys
sys.stdin = open("swea/[1208]Flatten.txt",'r')

T = int(input())
for t in range(1, T+1):
    dump = int(input())
    box = list(map(int, input().split()))
    while(dump > 0):
        high = max(box)
        low = min(box)
        box[box.index(high)] -= 1
        box[box.index(low)] += 1
        dump -= 1

    print("#{0} {1}".format(t, max(box)-min(box)))
