def solution(s):
    answer = ''
    idx = len(s) // 2 
    if len(s) % 2:
        answer = s[idx]
    else:
        answer = s[idx-1:idx+1]
    return answer
