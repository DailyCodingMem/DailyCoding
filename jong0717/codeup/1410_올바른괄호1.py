#20200908
bracket = list(map(str,input()))
# 여는 괄호 갯수 카운팅
left_cnt = 0
# 닫는 괄호 갯수 카운팅
right_cnt = 0
# bracket안에 돌면서
for bck in bracket:
    # 여는 괄호이면 left +1
    if bck == '(':
        left_cnt += 1
    # 닫는 괄호이면 right +1
    else:
        right_cnt += 1
print('{} {}'.format(left_cnt,right_cnt))