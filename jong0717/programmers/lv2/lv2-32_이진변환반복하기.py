def solution(s):
    zeroCnt = 0
    changeCnt = 0
    while s != '1':
        result = ''
        changeCnt += 1
        for i in s:
            if i != '0':
                result += i
            else:
                zeroCnt += 1
        s = len(result)
        # 접두어 제외하고 2진수로 바꿈.
        s = format(s,'b')
    answer = [changeCnt, zeroCnt]
    return answer
# 다른풀이 참고
def solution2(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
