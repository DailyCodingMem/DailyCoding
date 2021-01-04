def solution(phone_number):
    back_num = phone_number[-4:]
    answer = '*'*(len(phone_number)-4) + back_num
    return answer

