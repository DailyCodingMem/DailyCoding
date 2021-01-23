# swea - [10804]문자열의거울상 (2021-01-23)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXTC0x16D8EDFASe&categoryId=AXTC0x16D8EDFASe&categoryType=CODE
import sys
sys.stdin = open("swea/[10804]문자열의거울상.txt",'r')


T = int(input())
for t in range(1, T+1):
    word = input()
    tmp = ''
    for w in word :
        if w == 'b' :
            tmp += 'd'
        elif w == 'd' :
            tmp += 'b'
        elif w == 'p' :
            tmp += 'q'
        elif w == 'q' :
            tmp += 'p'
    print('#{0} {1}'.format(t,tmp[::-1]))