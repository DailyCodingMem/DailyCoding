
answers = [1,3,2,4,2]

P1=[]
P2=[]
P3=[]
for i in range(len(answers)):
    P1.append(i%5+1)
    if i%2: # i가 홀수일 때
        if i%8==1:
            P2.append(1)
        elif i%8==3:
            P2.append(3)
        elif i%8==5:
            P2.append(4)
        else:
            P2.append(5)
    elif not i%2: # i가 짝수일 때
        P2.append(2)
    if i%10<2:
        P3.append(3)
    elif i%10<4:
        P3.append(1)
    elif i%10<6:
        P3.append(2)
    elif i%10<8:
        P3.append(4)
    else:
        P3.append(5)
A1 = A2 = A3 = 0
for i in range(len(answers)):
    if answers[i] == P1[i]:
        A1 += 1
    if answers[i] == P2[i]:
        A2 += 1
    if answers[i] == P3[i]:
        A3 += 1
Max = max(A1,A2,A3)
answer = []
if Max == A1:
    answer.append(1)
if Max == A2:
    answer.append(2)
if Max==A3:
    answer.append(3)

print(answer)
