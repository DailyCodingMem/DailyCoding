def solution(x):
    result = 0
    for i in str(x):
        result += int(i)
    if x % result:
        return False
    return True

