def solution(s):
    answer = []
    for alpha in s:
        answer.append(alpha)
    answer.sort(reverse=True)

    return ''.join(answer)


