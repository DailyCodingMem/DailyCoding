import sys
sys.stdin = open("2309in.txt",'r')

def dwarf(i,result):
    global answer
    if len(result)==7:
        if sum(result) == 100:
            answer = result
        return
    else:
        for j in range(i,9):
            if visited[j]:
                visited[j] = False
                dwarf(j+1,result+[List[j]])
                visited[j] = True

List = list( int(input()) for _ in range(9))
visited = list(True for _ in range(9))
answer = []
dwarf(0,[])
answer.sort()
for i in answer:
    print(i)