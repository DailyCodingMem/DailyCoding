import sys
sys.stdin = open("1205in.txt",'r')

N , score, P = map(int,input().split())
ScoreList = list(map(int,input().split()))
ScoreList=list(map(int,sys.stdin.readline().split()))

ScoreList.sort(reverse=True)
try:
    if score in ScoreList:
        start = ScoreList.index(score)
        cnt = ScoreList.count(score)
        if start+1 <= P and start + cnt + 1 <= P:
            print(start+1)
        elif start+cnt + 1 > P:
            print(-1)
        elif start+1 > P:
            print(-1)

    else:
        for i in range(len(ScoreList)):
            if ScoreList[i] < score:
                if i+1 <= P:
                    print(i+1)
                else:
                    print(-1)
                break
        else:
            if i+2 <= P:
                print(i+2)
            else :
                print(-1)
except:
    print(1)
