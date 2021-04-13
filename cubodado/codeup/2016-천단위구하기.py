from collections import deque

num = int(input())
numbers = input()
answer = deque()
while numbers:
    if 3 <= len(numbers):
        answer.appendleft(',' + numbers[3:])
    else:
        answer.append(numbers)
print(answer)