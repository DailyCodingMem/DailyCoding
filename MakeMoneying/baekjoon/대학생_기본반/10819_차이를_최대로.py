import sys
sys.stdin = open("10819in.txt",'r')


def mySum(List):
    result = 0
    for i in range(len(List)-1):
        result += abs(List[i] - List[i+1])
    return result

def myList(List):
    global allList, visited
    if len(List)==N:
        allList.append(List)
        return

    for i in range(0,N):
        if visited[i]:
            visited[i] = False
            myList(List+[Array[i]])
            visited[i] = True

N = int(input())
Array = list(map(int,input().split()))
allList = []
visited = list(True for _ in range(N))
myList([])
Max = 0
for List in allList:
    result = mySum(List)
    if Max < result:
        Max = result
print(Max)