from itertools import combinations as comb
import math
def solution(nums):
    com_nums = list(comb(nums,3))
    cnt = 0
    for tp in com_nums:
        s_num = sum(tp)
        is_prime = True
        for i in range(2, int(math.sqrt(s_num)) + 1):
            if s_num % i == 0:
                is_prime = False
                break
        if is_prime:
            cnt += 1

    return cnt
