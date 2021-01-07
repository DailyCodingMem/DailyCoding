import sys
sys.stdin = open("11399in.txt",'r')

N = int(sys.stdin.readline())
myList = list(map(int, sys.stdin.readline().split()))
myList = sorted(myList, key=lambda x: x)
answer = 0
add = 0
for i in range(N):
    add += myList[i]
    answer += add
print(answer)