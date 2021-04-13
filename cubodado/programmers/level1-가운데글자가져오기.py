def solution(s):
    answer = ''
    length = len(s)
    half = length//2
    if length % 2:
        answer += s[half]
    else:
        answer += s[half-1:half+1]
    return answer