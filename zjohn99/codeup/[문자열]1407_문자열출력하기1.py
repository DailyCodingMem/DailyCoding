# codeup - 문자열 - 문자열출력하기1 (2020-09-04)
# https://codeup.kr/problem.php?id=1407

import sys
sys.stdin = open("codeup/[문자열]1407_문자열출력하기1.txt",'r')

T = int(input())
for _ in range(T):
    words = input()
    # 방법 1 : 리스트 변환후 join으로 합치기
    result = list(words.split())
    result = ''.join(result)

    # 방법 2 : replace 사용
    result = words.replace(' ', '')

    print(result)

    # 양쪽 공백을 없애는 함수 : strip // rstrip // lstrip