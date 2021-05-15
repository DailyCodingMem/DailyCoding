def quadzip(s):
    n = len(s)
    if n == 1:
        return s[0][0]
    temp = [[] for _ in range(n//2)]
    for i in range(1,n,2):
        for j in range(1,n,2):
            zero = s[i][j][0] + s[i][j-1][0] + s[i-1][j][0] + s[i-1][j-1][0]
            one = s[i][j][1] + s[i][j-1][1] + s[i-1][j][1] + s[i-1][j-1][1]
            # 압축
            if one == 0 :
                zero = 1
            if zero == 0 :
                one = 1
            temp[i//2].append([zero,one])
    return quadzip(temp)

def solution(arr):
    n = len(arr)
    first = [[] for _ in range(n//2)]
    # 초기 이차원 배열 만들기
    for i in range(1,n,2):
        for j in range(1,n,2):
            temp = [arr[i][j], arr[i][j-1], arr[i-1][j], arr[i-1][j-1]]
            one = temp.count(1)
            zero = temp.count(0)
            if one == 0:
                zero = 1
            if zero == 0:
                one = 1
            first[i//2].append([zero, one])
    return quadzip(first)
