# baekjoon - [1806]부분합 (2020-10-12)
# https://www.acmicpc.net/problem/1806

import sys
sys.stdin = open("baekjoon/[1806]부분합.txt",'r')

T = int(input())
for t in range(1, T+1):
   N, S = map(int, input().split())
   nums = list(map(int, input().split()))
   short_len = 100001
   start = 0
   end = 0

   val = nums[start]
   while(start < N) :
      if val >= S :
         short_len = min(short_len, end - start + 1)
         val -= nums[start]
         start += 1
      else :
         if end + 1 != N :   
            end += 1
            val += nums[end]
         else :
            start += 1
   if short_len == 100001 :
      print(0)
   else : 
      print(short_len)




# N, M = map(int, input().split())

# user_input = list(map(int, input().split()))

# end = 0
# count = 0
# answer = 100000001
# for start in range(N):
#     while count < M and end < N:
#         count += user_input[end]
#         end += 1
#     if count >= M and answer > end - start:
#         answer = end - start
#     count -= user_input[start]

# if answer == 100000001:
#     answer = 0
# print(answer)





      
      

       
