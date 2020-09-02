ternell = list(map(int, input().split(' ')))
answer = ''
# 차가 170
for t in range(len(ternell)):
    if ternell[t] <= 170:
        answer = 'CRASH'
        break
    elif 170 <= ternell[t] and t == (len(ternell) - 1):
        answer = 'PASS'
print(answer)