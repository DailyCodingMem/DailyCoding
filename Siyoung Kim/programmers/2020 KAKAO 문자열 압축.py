import math


def solution(s):
    answer = float('inf')
    for leng in range(1, math.ceil(len(s) / 2) + 1):
        tmpans = ''
        before = ''
        cnt = 1

        # print('#',leng,end=' ')
        for i in range(0, len(s), leng):
            now = s[i:i + leng]
            if now == before:
                cnt += 1
            else:
                if cnt == 1:
                    tmpans += before
                else:
                    tmpans += str(cnt) + str(before)
                before = now
                cnt = 1
        if cnt == 1:
            tmpans += before
        else:
            tmpans += str(cnt) + str(before)
        # print(tmpans)
        if len(tmpans) < answer:
            answer = len(tmpans)
    return answer
