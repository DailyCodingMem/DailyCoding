import sys
sys.stdin = open("8979in.txt",'r')

import sys
N,K = map(int,sys.stdin.readline().split())
countries = list(list(map(int,sys.stdin.readline().split())) for _ in range(N))
countries = sorted(countries, key=lambda x:(-x[1],-x[2],-x[3]))
index = 0
for i in range(N):
    if K == countries[i][0]:
        index = i
start = index
while True:
    try:
        if countries[start][1:] == countries[index][1:]:
            start -= 1
        else:
            break

    except:
        break
print(start+2)
