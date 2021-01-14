def solution(s, n):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i].isupper():
            s_list[i] = chr((ord(s_list[i]) - ord("A") + n) % 26 + ord("A"))
        elif s_list[i].islower():
            s_list[i] = chr((ord(s_list[i]) - ord("a") + n) % 26 + ord("a"))
    return ''.join(s_list)

