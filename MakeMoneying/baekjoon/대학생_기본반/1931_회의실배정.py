import sys
sys.stdin = open("1931in.txt",'r')

N = int(input())
Max = 0
myList = []
answer = 0
for _ in range(N):
    A,B = map(int,input().split())
    myList.append((A,B))
myList = sorted(myList, key=lambda x: x[0])
myList = sorted(myList, key=lambda x: x[1])
start = last = 0
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
for i in range(len(myList)):
    if myList[i][0] >= last:
        answer += 1
        start = myList[i][0]
        last = myList[i][1]
print(answer)