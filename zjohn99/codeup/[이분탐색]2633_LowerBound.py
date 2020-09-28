# codeup - 이분탐색 - LowerBound (2020-09-28)
# https://codeup.kr/problem.php?id=2633

import sys
sys.stdin = open("codeup/[이분탐색]2633_LowerBound.txt",'r')


def solution(start, mid, end):
    if start == mid :
        return start + 1 
    if k >= num[mid] :
        return solution(mid, (mid+end)//2, end)
    elif k < num[mid] :
        return solution(start, (start+mid)//2, mid)
    # else :
    #     # same_val = num.count(k) - 1
    #     tmp = mid
    #     while(True) :
    #         tmp -= 1
    #         if tmp < 0 :
    #             return 1
    #         if num[tmp] != k :
    #             return mid+1

    
## 123 4 6 67

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    
    # tmp = num.index(k) + 1 # index 활용
    # print(tmp)
    if num[n-1] < k :
        print(n+1)
    else :
        print(solution(0, n//2, n))
