# 20200907
origin = list(map(str,input()))
# 첫번째 방법 저장
ans1 = []
# 두번째 방법 저장
ans2 = []
for alp in origin:
    # 첫번째 방법대로 계산 ascii변환 이용 
    # chr : 아스키코드를 문자나 숫자로
    # ord : 문자나 숫자를 아스키코드로
    ans1.append(chr(ord(alp) + 2))
    ans2.append(chr((ord(alp) * 7) % 80 + 48))
print(''.join(ans1))
print(''.join(ans2))