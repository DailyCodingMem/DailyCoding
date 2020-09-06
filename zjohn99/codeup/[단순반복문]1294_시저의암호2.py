# codeup - 단순반복문 - 시저의암호2 (2020-09-05)
# https://codeup.kr/problem.php?id=1294

import sys
sys.stdin = open("codeup/[단순반복문]1294_시저의암호2.txt",'r')

T = int(input())
for _ in range(T):
  text = input()
  code = ''
  for i in range(len(text)):
    if text[i] != ' ':
        if ord(text[i])+3 > 122 :
            code += chr(96 + (122 - ord(text[i])+3))
        else :
            code += chr(ord(text[i])+3)
    else :
        code += " "

  print(code)
