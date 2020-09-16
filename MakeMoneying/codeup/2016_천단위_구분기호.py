# 9
# 123456789

N = int(input())
Number = input()
Length = N + N//3
if N%3: # celi
    Length += 1
Answer = ''
Cnt = 0
for i in range(Length-1):
    if i%4==3: # 3번째 일 때 마다
        Answer = ',' + Answer
        Cnt += 1
    else:
        Answer = Number[len(Number)-1-i+Cnt] + Answer
print(Answer)