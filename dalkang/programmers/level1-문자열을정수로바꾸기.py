def solution(s):
    answer = ''
    for S in s:
        if S == '-':
            answer += '-'
        else:
            answer += S
            
    return int(answer)