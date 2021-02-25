def solution(s):
    answer = []
    s_list = s.split(' ')
    # title 함수를 이용해도 됨. title은 문장에 적용, capitalize는 단어에 적용
    for word in s_list:
        answer.append(word.capitalize())
    return ' '.join(answer)
