def solution(n):
    one_cnt = bin(n).count('1')
    for i in range(n+1,1000001):
        if bin(i).count('1') == one_cnt:
            return i

n = 78
print(bin(n))
print(bin(n).count('1'))
one_cnt = bin(n).count('1')
# for i in range(n+1,1000001):
#     if bin(i).count('1') == one_cnt:
#         # print(i)
print(solution(n))