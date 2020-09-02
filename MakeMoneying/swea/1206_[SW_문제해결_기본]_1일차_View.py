import sys
sys.stdin = open("1206in.txt",'r')
 
def building(cnt,idx): # cnt는 왼쪽에서 몇번째 건물인지, idx는 빌딩의 층수
    global Answer
    if List[cnt-1] >= idx or List[cnt-2]>=idx or List[cnt+1]>=idx or List[cnt+2]>=idx: 
        # 왼쪽으로 한칸 두칸, 오른쪽으로 한칸 두칸 봐서 idx 이상의 층수가 있으면 바로 돌아가!!
        return
    else:
        Answer += 1 # 왼쪽 오른쪽 봣는데 막힌게 없으면 answer값은 1 증가시키고 
        building(cnt,idx-1) # 한 층 줄여서 실행


for Count in range(10):
    N = int(input())
    List = list(map(int,input().split()))
    Answer = 0
    for i in range(N):
        if List[i]: # 0이 아닐 때만 실행되도록 
            building(i,List[i])
    print("#{} {}".format(Count+1,Answer))
    