from itertools import combinations as combs
import math
T = int(input())
for _ in range(T):
    s = []
    answer = 0
    nums = list(map(int,input().split(' ')))
    nums.pop(0)
    s.extend(combs(nums,2))
    for pair in s:
        answer += math.gcd(pair[0],pair[1])
    print(answer)