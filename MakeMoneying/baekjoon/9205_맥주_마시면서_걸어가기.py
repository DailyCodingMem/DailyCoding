import sys
sys.stdin = open("9205in.txt",'r')

from collections import deque

def goFesti(y,x):
    global visitedStore
    basket = deque([(y,x)])
    while basket:
        newY,newX = basket.popleft()
        if abs(festiY-newY) + abs(festiX-newX) <= 1000:
            return "happy"
        for i in range(len(visitedStore)):
            if visitedStore[i] and (abs(store[i][0]-newY) + abs(store[i][1]-newX) <= 1000):
                visitedStore[i] = False
                basket.append((store[i][0],store[i][1]))
    return "sad"
        

T = int(input())
for count in range(T):
    N = int(input())
    startY,startX = map(int,input().split())
    store = []
    for _ in range(N):
        A,B = map(int,input().split())
        store.append((A,B))
    visitedStore = list(True for _ in range(N))
    festiY,festiX = map(int,input().split())
    print(goFesti(startY,startX))