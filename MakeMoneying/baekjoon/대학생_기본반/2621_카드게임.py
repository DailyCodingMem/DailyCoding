import sys
sys.stdin = open("2621in.txt",'r')

numberList = {}
for i in range(1,10):
    numberList[i] = []
colorList = { 
    'R':[], 
    'B':[], 
    'Y':[], 
    'G':[]
}
cards = []
for _ in range(5):
    A,B = input().split()
    cards.append(B)
    colorList[A].append(B)
    numberList[int(B)].append(A)
for myList in colorList:
    colorList[myList].sort()
cards.sort()

# 1. 5개 색 같고 스트레이트 +900 + 가장 높은 수
# 2. 4개 숫자 같다 +800 + 수
# 3. 3개 숫자 같고 나머지 2개도 같다 + 700 + 10*a + b
# 4. 5개 색 같다. + 600 + 가장 높은 수
# 5. 5개 숫자 스트레이트  +500 + 가장 높은 수
# 6. 3개 숫자 같다. +400 + 수
# 7. 2개 숫자 같고 또 다른 숫자 2개 같다. +300 + 높은수*10 + 낮은 수
# 8. 2개 숫자 같다 + 200 + 수

# 9. 아무것도 아니다 + 100 + 가장 높은 수
def check(colorList,numberList,cards):
    score = 0
    for i in colorList:
        if len(colorList[i])==5:
            if int(colorList[i][0])+4 == int(colorList[i][4]):
                return 900+int(colorList[i][4])
            else:
                score = max(score,600 + int(colorList[i][len(colorList[i])-1]))

    for i in numberList:
        if len(numberList[i])>=4:
            return 800 + i
        elif len(numberList[i]) == 3:
            for j in range(1,10):
                if len(numberList[j])==2:
                    score = max(score,700+10*i+j)
            score = max(score, 400 + i)
        elif len(numberList[i])==2:
            for j in range(i+1,10):
                if len(numberList[j])==2:
                    score = max(score, 300 + 10*j + i)
            score = max(score, 200 + i)
                
        
    for i in range(1,6):
        if numberList[i] and numberList[i+1] and numberList[i+2] and numberList[i+3] and numberList[i+4]:
            score = max(score,500+i+4)
    
    score = max(score, 100+int(cards[-1]))
    return score

print(check(colorList,numberList,cards))