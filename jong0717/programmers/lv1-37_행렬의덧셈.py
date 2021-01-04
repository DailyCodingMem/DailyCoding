def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr2))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution([[1],[2]],[[3],[4]]))


import numpy as np
def sumMatrix(A,B):
    # np.array를 이용해 list를 array로
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    # tolist로 array를 list로
    return answer.tolist()


def sumMatrix2(A,B):
    # zip은 두개의 list를 하나의 연관 리스트로 만들어줌
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

