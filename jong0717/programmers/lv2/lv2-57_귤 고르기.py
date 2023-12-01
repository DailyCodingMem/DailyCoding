def solution(k, tangerine):
    answer = 0
    tan_dict = dict()
    for i in tangerine:
        if i in tan_dict:
            tan_dict[i] += 1
        else:
            tan_dict[i] = 1
    tan_dict = dict(sorted(tan_dict.items(), key=lambda x: x[1], reverse=True))
    print(tan_dict)
    for i in tan_dict:
        if k <= 0:
            return answer
        k -= tan_dict[i]
        answer += 1
    return answer


tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 6
print(solution(k, tangerine))
