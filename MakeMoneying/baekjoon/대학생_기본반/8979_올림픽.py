import sys
sys.stdin = open("8979in.txt",'r')

N,Country = map(int,input().split())
List = []
while N:
    count,gold,silver,bronze = map(int,input().split())
    for i in range(len(List)):
        if List[i][1] < gold:
            List.insert(i,[count,gold,silver,bronze])
            break
        elif List[i][1] == gold and List[i][2] < silver:
            List.insert(i,[count,gold,silver,bronze])
            break
        elif List[i][1] == gold and List[i][2] == silver and List[i][3] < bronze:
            List.insert(i,[count,gold,silver,bronze])
            break
        elif List[i][1] == gold and List[i][2] == silver and List[i][3] == bronze:
            List.insert(i,[count,gold,silver,bronze])
            break
    else:
        List.append([count,gold,silver,bronze])
    N -= 1
for i in range(len(List)):
    if Country == List[i][0]:
        point = i
        while True:
            if 0<= point-1:
                if List[point][1] == List[point-1][1] and List[point][2] == List[point-1][2] and List[point][3] == List[point-1][3]:
                    point -= 1
                else:
                    break
            else:
                break
        print(point+1)
        break