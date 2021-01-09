import sys
sys.stdin = open("2003.txt",'r')

n,m = map(int,sys.stdin.readline().split())
myList = list(map(int,sys.stdin.readline().split()))
head = answer = 0
tail = 1
mySum = myList[0]
while True:
    try:
        if mySum == m or head == tail:
            if mySum == m:
                answer += 1
            head += 1
            tail = head + 1
            mySum = myList[head]
            continue
        if head == n-1:
            break

        if mySum < m:
            mySum += myList[tail]
            tail += 1
        elif mySum > m:
            mySum -= myList[head]
            head += 1
        
    except:
        break
print(answer)