import sys
sys.stdin = open("1931in.txt",'r')

N = int(input())
myList = []
answer = 0
for _ in range(N):
    A,B = map(int,input().split())
    myList.append((A,B))
myList = sorted(myList, key=lambda a:a[0])
myList = sorted(myList, key=lambda a:a[1])
print(myList)