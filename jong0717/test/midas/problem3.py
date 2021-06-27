


def solution(N,K,T):
    T.sort()
    T = sorted(T, key=lambda x:x[1])
    cnt = 0
    K_time = [1]*K
    for t in T:
        for i in range(t[0]-1,t[1]):
            if K_time[i] == 1:
                K_time[i] = 0
                cnt += 1
                break
    return cnt

N = 4
K = 4
T = [[1,5],[1,3],[1,1]]
Tsort = sorted(T, key=lambda x: x[0])
Tsort2 = sorted(Tsort, key=lambda x : x[1])
print(T)
cnt = 0
K_time = [1 for _ in range(K)]
for t in T:
    for i in range(t[0]-1,t[1]):
        if K_time[i] == 1:
            K_time[i] = 0
            cnt += 1
            break
