
def solution(brown, yellow):
    for i in range(3,(brown+yellow)//3+1):
        Y = i
        if not (brown+yellow)%Y: # 정수이면
            X = (brown+yellow)//Y # X값을 구한다
            if not yellow%(Y-2): # yellow를 (Y-2)나눈 값이 정수이면
                yellowY = Y-2
                if not (yellow)%yellowY and yellow//yellowY < X: # yellow를 yellowY로 나눴을 때 정수이면
                    answer = [X,Y]
                    return answer


brown = 10
brown = 8
brown = 24
yellow = 2
yellow = 1
yellow = 24
print(solution(brown,yellow))
print(solution(8,1))
