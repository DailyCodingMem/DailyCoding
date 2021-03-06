N = int(input())
# 2진법을 표기하기위한 앞 부분
b_num = 0b1
'''format(number, [notation]) >> notation에 b를 주면 2진법으로, x를 주면 16진법으로 변환
default 값은 10이고 number에는 int자료형이 들어가야하고 출력은 str이기 때문에
다시 int로 변환해서 저장해준다.'''
d_num = int(format(b_num, "b"))
while 1:
    # 2진법으로 표현된 수가 N으로 나누어떨어지면 출력하고 break
    if d_num % N == 0:
        print(d_num)
        break
    # 1씩 더해가면서 2진법으로 변환
    b_num += 1
    d_num = int(format(b_num, "b"))
    # 값 초과하면 0 출력하고 break
    if d_num >= 2**64:
        print(0)
        break
