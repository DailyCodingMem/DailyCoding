# swea - [10912]외로운문자 (2021-01-22)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXVJuEvqLAADFASe&categoryId=AXVJuEvqLAADFASe&categoryType=CODE
import sys
sys.stdin = open("swea/[10912]외로운문자.txt",'r')

# 투포인터

T = int(input())
for t in range(1, T+1):
    word = input()

    dic = {}

    for i in range(len(word)) :
        if word[i] in dic :
            dic[word[i]] += 1
        else :
            dic[word[i]] = 1
    result = ''
    for key, val in dic.items() :
        if val % 2 : # 2로 나눴을때 나머지가 0이 아니면
            result += key
    result = list(result)
    result.sort()
    if len(result) == 0 :
        result = ['Good']
    print('#{0} {1}'.format(t, ''.join(result)))
