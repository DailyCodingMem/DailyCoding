def solution(a, b):
    arr = list(range(a, b+1))
    if a > b:
        arr = list(range(b, a+1))
    answer = sum(arr)
    if a == b:
        answer = a
    return answer