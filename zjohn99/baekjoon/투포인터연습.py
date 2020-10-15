# 투포인터 연습 (2020-10-14)

import sys
sys.stdin = open("baekjoon/투포인터연습.txt",'r')

T = int(input())
for t in range(1, T+1):
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    # start = 0
    # end = 0
    # cnt = 0
    # val = nums[start]

    # while(start < N) :
    #     if val >= S :
    #         if val == S :
    #             cnt += 1
    #         val -= nums[start]
    #         if start == end and end+1 != N: 
    #             end += 1
    #         start += 1
    #     else : # val < S
    #         if end+1 != N :
    #             end += 1
    #             val += nums[end]
    #         else :
    #             start += 1
    # print(cnt)

# 방법 2
    cnt = 0
    val = 0
    end = 0

    # start를 차례대로 증가시키며 반복
    for start in range(N) :
        # end를 가능한 만큼 이동시키기
        while val < S and end < N :
            val += nums[end]
            end += 1
        
        # 부분합이 S 일때 카운트 증가
        if val == S :
            cnt += 1
        
        val -= nums[start]
    
    print(cnt)



            
