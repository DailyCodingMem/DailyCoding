import sys
sys.stdin = open("1987in.txt",'r')

from queue import Queue
sys.setrecursionlimit(10**5)

dy = [-1,1,0,0]
dx = [0,0,-1,1]
R,C = map(int,input().split())
alpha = list(list(x for x in input()) for _ in range(R))
basket = Queue([(0,0,alpha[0][0])])
answer = 1
while basket:
    newY,newX,alphabet = basket.get()
    for i in range(4):
        checkY = newY + dy[i]
        checkX = newX + dx[i]
        if 0<=checkY<R and 0<=checkX<C and (alpha[checkY][checkX] not in alphabet):
            basket.put((checkY,checkX,alphabet+alpha[checkY][checkX]))
            answer = max(answer,len(alphabet)+1)
print(answer)