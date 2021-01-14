from string import ascii_lowercase
def solution(s):
    alpha = list(ascii_lowercase)
    answer = True
    for i in s:
        if i in alpha:
            answer = False
        else:
            if len(s) != 4 and len(s) != 6: 
                answer = False
    return answer