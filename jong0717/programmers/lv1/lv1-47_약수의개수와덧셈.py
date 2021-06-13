def division(n):
    result = 0
    for i in range(1,n+1):
        if n % i == 0:
            result += 1
    return result

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if division(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


