def solution(survey, choices):
    answer = ''
    char = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for s, c in zip(survey, choices):
        if c > 4:
            char[s[1]] = c - 4
        else:
            char[s[0]] = 4 - c

    char_list = list(char.items())
    for i in range(0, 8, 2):
        if char_list[i][1] < char_list[i+1][1]:
            answer += char_list[i+1][0]
        else:
            answer += char_list[i][0]
    return answer