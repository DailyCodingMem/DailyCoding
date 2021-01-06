import sys
sys.stdin = open("2529in.txt",'r')

def checkList(List,cnt):
    global basket
    if cnt == N:
        basket.append(List)
        return


    for i in range(10):
        if visited[i]:
            if not len(List):
                visited[i] = False
                checkList(List + [Number[i]],cnt)
                visited[i] = True

            else:
                if arrow[cnt] == ">":
                    if List[-1] > Number[i]:
                        visited[i] = False
                        checkList(List + [Number[i]],cnt+1)
                        visited[i] = True
                else:
                    if List[-1] < Number[i]:
                        visited[i] = False
                        checkList(List + [Number[i]],cnt+1)
                        visited[i] = True

N = int(input())
arrow = list(input().split())
Number = list(x for x in range(10))
visited = list(True for _ in range(10))
basket = []
checkList([],0)
answer1 = ""
answer2 = ""
for i in basket[0]:
    answer1 += str(i)
for i in basket[-1]:
    answer2 += str(i)
print(answer2)
print(answer1)