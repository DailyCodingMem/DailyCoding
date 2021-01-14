def solution(n):
    answer = ''
    while n >= 1:
        # 몫을 n으로 해주어야 계속 적으로 n을 3으로 나눠주면서 계산이됨
        n, r = divmod(n,3)
        answer += str(r)
    answer = int(answer,3)
    return answer

print(solution(45))