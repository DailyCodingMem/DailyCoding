# codeup - 단순반복문 - 홀수더하고짝수빼고3 (2020-09-02)
# https://codeup.kr/problem.php?id=1281

import sys
sys.stdin = open("codeup/[단순반복문]1281_홀수더하고짝수빼고3.txt",'r')

T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    tmp = 0
    result = ""
    for n in range(a, b+1):
        if n%2 != 0 : # 짝수일 때,
            if n == a :
                result += "{0}".format(n)
            else :
                result += "+{0}".format(n)
            tmp += n
        else : # 홀수일 때,
            result += "-{0}".format(n)
            tmp -= n
    else:
        result += "={0}".format(tmp)
    print(result)

