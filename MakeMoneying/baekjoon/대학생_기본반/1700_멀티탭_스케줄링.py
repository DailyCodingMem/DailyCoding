import sys
sys.stdin = open("1700in.txt",'r')

N,K = map(int, input().split())
items = list(map(int, input().split()))

socket = list(0 for _ in range(N))
cnt = 0
for l in range(len(items)):
    
    for i in range(len(socket)):
        if not items[l] in socket:
            if socket[i] == 0:
                socket[i] = items[l]
                break
        else:
            break
    else:
        a = 0
        for j in range(N): 
            try:
                if a < items[l+1:].index(socket[j]):
                    a = items[l+1:].index(socket[j])
                    idx = j
            except:
                idx = j
                break
        socket[idx] = items[l]
        cnt += 1

print(cnt)