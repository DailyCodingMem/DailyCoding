import sys
sys.stdin = open("in.txt",'r')

N = int(input())
List = []
for _ in range(N):
    List.append(int(input()))
answer = 0
basket = [List[0]]
for i in range(1,N):
    if basket[-1] > List[i]:
        answer += len(basket)
        basket.append(List[i])
    else:
        while True:
            if basket:
                A = basket.pop()
                if A > List[i]:
                    basket.append(A)
                    answer += len(basket)
                    basket.append(List[i])
                    break
            else:
                basket = [List[i]]
                break
print(answer)