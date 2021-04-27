# 로또 당첨 등수 매기기
# 혹은 리스트로 그냥 [6,6,5,4,3,2,1]해놓고 인덱스 접근해도될듯
def Winning(n):
    rank = 0
    if 1 < n < 7:
        rank = 7 - n
    else :
        rank = 6
    return rank
def solution(lottos, win_nums):
    # 일치하는 최대,최소 갯수를 저장할 리스트
    # 애초에 최대에 해당하는 값을 count함수로 0의 갯수를 저장해두면 elif절은 필요없음.
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

