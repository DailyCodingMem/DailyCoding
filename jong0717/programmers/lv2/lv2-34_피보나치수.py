# 실패의 과정들....ver1~3
# memo = [0,1]
# def solution1(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(memo[n-1]+memo[n-2])
#     return memo[n] % 1234567       

# dic = {1:1, 2:1}
# def solution2(n):
#     if n in dic:
#         return dic[n]
    
#     dic[n] = solution2(n-1) + solution2(n-2)
#     return dic[n]

# def solution3(n):
#     solutionList=[0, 1]
#     if n==1:
#         return 0
#     elif n ==2 :
#         return 1
#     for i in range(2,n):
#         solutionList.append(solutionList[i-1] + solutionList[i-2] )
#     return solutionList[n] % 1234567

# 하 메모이제이션..도전했는데 결국..
def solution(n):
    pre, cur = 0, 1
    for i in range(1,n):
        pre, cur = cur, pre+cur
    return cur % 1234567