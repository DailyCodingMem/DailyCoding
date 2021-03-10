from string import ascii_lowercase
def solution(new_id):
    answer = ''
    # 1단계 소문자 치환
    id_list = list(new_id.lower())
    # 2단계 사용불가 문자 제거
    possible_list = [str(i) for i in range(10)] + ['.','_','-']
    for i in id_list:
        if i not in possible_list and i not in ascii_lowercase:
            continue
        else:
            answer += str(i)
    # 3단계 연속된 마침표 치환
    while '..' in answer:
        answer = answer.replace('..','.')
    # 4단계 처음과 끝의 마침표 제거
    try:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 5단계 빈문자열이면 a 대입 
    except:
        if answer == '':
            answer = 'a'
    # 6단계 길이는 15까지
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계 길이는 최소3
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    return answer

