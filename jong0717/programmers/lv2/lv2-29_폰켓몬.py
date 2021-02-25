def solution(nums):
    N = len(nums)
    n_set = set(nums)
    return min(len(n_set),N//2)
