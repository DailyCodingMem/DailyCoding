# 20200908
N = int(input())
# 주사위 2개 셋팅
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
# dice1을 돌면서
for num in dice1:
    # N에서 num을 뺀 값이 dice2에 있으면 출력
    if N-num in dice2:
        print('{} {}'.format(num,N-num))