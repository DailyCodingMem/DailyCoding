def solution(a, b):
    numbers = [x for x in range(min(a,b),max(a,b)+1)]
    answer = sum(numbers)
    return answer