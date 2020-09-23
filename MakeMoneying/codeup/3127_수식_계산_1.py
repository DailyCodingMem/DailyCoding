import sys
sys.stdin = open("in.txt",'r')

from collections import deque

List = list(input().split())
deq = deque(List)
basket = deque([])
while deq:
    A = deq.popleft()
    if A.isdigit():
        basket.append(A)
    else:
        one = int(basket.pop())
        two = int(basket.pop())
        if A=="+":
            basket.append(one+two)
        elif A=="-":
                basket.append(two-one)
        elif A=="*":
                basket.append(one*two)
        
print(basket.pop())
