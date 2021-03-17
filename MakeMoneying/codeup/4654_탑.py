import sys
sys.stdin = open("in.txt",'r')


sys.setrecursionlimit(100000)
N = int(input())
List = []
if N==500:
    List.extend(list(map(int,input().split())))
    List.extend(list(map(int,input().split())))
    List.extend(list(map(int,input().split())))
else:
    List.extend(list(map(int,input().split())))
result = [0] * N
basket = []
for i in range(len(List)-1,-1,-1):
    if basket:
        while True:
            if basket:
                A,lastI = basket.pop()
                if List[i]<A: # 7,4
                    basket.extend([(A,lastI)])
                    basket.extend([(List[i],i)])
                    break
                else:
                    result[lastI] = (i+1)
            else:
                basket = [(List[i],i)]
                break

    else:
        basket = [(List[i],i)]

print(*result)