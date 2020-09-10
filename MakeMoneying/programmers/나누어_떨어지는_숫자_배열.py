def solution(arr, divisor):
    answer = []
    for i in arr:
        if not i%divisor:
            answer.append(i)
    if len(answer):
        answer.sort()

    else:
        answer = -1

    return answer

arr = [5, 9, 7, 10]
divisor = 5
solution(arr,divisor)