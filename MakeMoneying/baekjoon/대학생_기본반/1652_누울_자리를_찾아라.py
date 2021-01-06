import sys
sys.stdin= open("1652in.txt", 'r')


from collections import deque
N = int(input())
List = list(list(x for x in input()) for _ in range(N))
# [['.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['.', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']]
visitedVertical = list(list(True for _ in range(N)) for _ in range(N))
visitedHorizon = list(list(True for _ in range(N)) for _ in range(N))

answerVertical = 0
answerHorizon = 0

for y in range(N):
    for x in range(N):
        if visitedVertical[y][x] and List[y][x] == ".":
            basket = deque([(y, x)])
            while True:
                newY, newX = basket[-1]
                newY += 1
                if 0 <= newY < N and List[newY][newX]==".":
                    basket.append((newY, newX))
                else:
                    break
            if len(basket) >= 2:
                answerVertical += 1
                while basket:
                    Y, X = basket.pop()
                    visitedVertical[Y][X] = False
        if visitedHorizon[y][x] and List[y][x] == ".":
            basket = deque([(y, x)])
            while True:
                newY, newX = basket[-1]
                newX += 1
                if 0<= newX < N and List[newY][newX]==".":
                    basket.append((newY,newX))
                else:
                    break
            if len(basket) >= 2:
                answerHorizon += 1
                while basket:
                    Y, X = basket.pop()
                    visitedHorizon[Y][X] = False
print(answerHorizon, answerVertical)
