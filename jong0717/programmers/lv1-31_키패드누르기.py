def solution(numbers, hand):
    answer = ''
    left_loc = 10
    right_loc = 12   
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_loc = num
        elif num in [3,6,9]:
            answer += 'R'
            right_loc = num
        else:
            num = 11 if num == 0 else num
            # 아래로 가면서 3씩 커져서 차이를 3으로 나눈 몫과 나머지를 더하면 거리가됨
            L_dis = sum(divmod(abs(num-left_loc),3))
            R_dis = sum(divmod(abs(num-right_loc),3))
            if L_dis > R_dis:
                answer += 'R'
                right_loc = num
            elif L_dis < R_dis:
                answer += 'L'
                left_loc = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left_loc = num
                else:
                    answer += 'R'
                    right_loc = num
    return answer
'''key_dict = {1:(0,0),2:(0,1),3:(0,2),
    4:(1,0),5:(1,1),6:(1,2),
    7:(2,0),8:(2,1),9:(2,2),
    '*':(3,0),0:(3,1),'#':(3,2)}
    자판에대한 좌표를 저장해서 딕셔너리 key로 접근해서 거리계산해도 쉬움'''