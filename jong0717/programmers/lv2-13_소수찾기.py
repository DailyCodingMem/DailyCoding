from itertools import combinations
def solution(numbers):
    answer = 0
    nums = []
    for num in numbers:
        nums.append(num)
    perm = list(combinations(nums,2))
    print(perm)
    return answer