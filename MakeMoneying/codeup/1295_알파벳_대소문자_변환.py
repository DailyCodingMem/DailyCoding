import sys
sys.stdin =open("1295in.txt",'r')

String = input()
Answer = ''
for i in String:
    if ord(i)>=97: # 소문자 이면
        Answer += i.upper() #대문자로
    else:
        Answer += i.lower() # 소문자로
print(Answer)