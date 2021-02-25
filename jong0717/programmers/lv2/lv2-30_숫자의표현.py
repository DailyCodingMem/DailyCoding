def solution(n):
    cnt = 0
    for i in range(1,n):
        s = i
        for j in range(i+1,n):
            s += j 
            if s == n:
                cnt += 1
                break
            elif s > n:
                break         
    return cnt+1