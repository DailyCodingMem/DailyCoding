# 20200907
'''생년월일과 몇년도 출생인지 구별하는걸 str으로 받음 
int로 받으면 slicing을 할 수 없어서 저렇게 받음'''
birth, gen = map(str,input().split())
# 기준이 되는 해를 할당
now = 2012
# birth가 문자열이니까 slicing한다음 int로 변환해서 저장
celb = int(birth[:2])
'''처음에 1 or 2로 했는데 수학에서의 의미와 달라서 원하는대로 처리가
안되서 사이값으로 확인'''
if 1<= int(gen) <= 2:
    # 1이나 2면 1900을 빼주고 +1
    age = now - 1900 - celb + 1
    # 3이나 4면 2000빼주고 +1 실은 그냥 1999빼면되는데 더 직관적으로 보여주려고
else :
    age = now - 2000 - celb + 1
print(age)
