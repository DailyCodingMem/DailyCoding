import sys
sys.stdin = open("1281in.txt",'r')

A,B = map(int,input().split())
Answer = '' # 스트링 형태로 저장
total = 0
for i in range(A,B+1):
    total += (-1)**(i+1) * i
    if i == A: # 처음에만 부호 안 넣고 바로 Answer에 연결
        Answer = str((-1)**(i+1)*i)
    else: # 처음을 제외하고 나머지애들
        if i%2: # 홀수이면
            Answer += ('+' + str(i))
        else: # 짝수 이면
            Answer += ('-' + str(i))
print("{}={}".format(Answer,total))