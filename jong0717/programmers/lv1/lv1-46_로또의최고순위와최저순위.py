# 로또 당첨 등수 매기기
def Winning(n):
    rank = 0
    if 1 < n < 7:
        rank = 7 - n
    else :
        rank = 6
    return rank
def solution(lottos, win_nums):
    # 일치하는 최대,최소 갯수를 저장할 리스트
    result = [0,0]
    for lotto in lottos:
        # 일치하는 숫자 갯수를 최대,최소에 우선 저장
        if lotto in win_nums:
            result[0] += 1
            result[1] += 1
        # 0의 경우가 추가로 맞출수있는 번호 이므로 0의 갯수를 더해줌
        elif lotto == 0:
            result[0] += 1
    return [Winning(result[0]), Winning(result[1]))]

