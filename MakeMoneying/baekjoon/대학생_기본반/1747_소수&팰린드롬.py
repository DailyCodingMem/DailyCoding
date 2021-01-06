import sys
sys.stdin = open("1747in.txt",'r')

N = int(input())
decimal = [True] * 1050001
decimal[1] = False
def findDec():
    for i in range(2,len(decimal)):
        if decimal[i]:
            for j in range(2*i,len(decimal),i):
                decimal[j] = False
findDec()
def findPel(N):
    for i in range(N,len(decimal)):
        if decimal[i]:
            myString = str(i)
            if myString == myString[::-1]:
                return i
print(findPel(N))