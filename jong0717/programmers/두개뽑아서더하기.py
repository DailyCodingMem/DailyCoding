def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            S_num = numbers[i] + numbers[j]
            if S_num not in answer:
                answer.append(S_num)
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))