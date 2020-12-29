#20200910
def solution(arr, divisor):
    answer = []
    for n in arr:
        if n % divisor == 0:
            answer.append(n)
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer