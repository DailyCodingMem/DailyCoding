def solution(s):
    answer = True
    s_low = s.lower()
    if s_low.count('p') == 0 and s_low.count('y') == 0 :
        return True
    elif s_low.count('p') != s_low.count('y'):
        answer = False
    return answer

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')