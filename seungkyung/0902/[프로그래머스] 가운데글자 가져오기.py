def solution(s):
    answer = ''
    center = len(s)//2
    if len(s)%2==0:
        answer = s[center-1]+s[center]
    else:
        answer = s[center]
    return answer