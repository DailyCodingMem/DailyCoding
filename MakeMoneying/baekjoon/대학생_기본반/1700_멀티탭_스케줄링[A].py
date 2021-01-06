import sys
sys.stdin = open("1700in.txt",'r')

n, k = map(int, input().split())
List = list(map(int, input().split()))
m = [0 for i in range(n)]
cnt = 0
for i in range(k):
    isTrue = False
    for j in range(n):
        if m[j] == List[i] or m[j] == 0:
            isTrue = True
            m[j] = List[i]
            break
    if isTrue:
        continue
    else:
        a = 0
        for j in range(n):
            try:
                if a < List[i + 1:].index(m[j]):
                    a = List[i + 1:].index(m[j])
                    b = j
            except:
                a = -1
                b = j
                break
        m[b] = List[i]
        cnt += 1
print(cnt)