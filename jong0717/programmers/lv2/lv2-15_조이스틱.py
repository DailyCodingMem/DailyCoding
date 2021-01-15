from string import ascii_lowercase
def solution(name):
    answer = 0
    alpha = list(ascii_lowercase.upper())
    n = len(name)
    side_cnt = n - 1
    for i in name:
        idx = alpha.index(i)
        if idx > 13:
            answer += 26 - idx
        else:
            answer += idx
    for c in range(n):
        _next = c + 1
        while _next < n and name[_next] == 'A':
            _next += 1
        side_cnt = min(side_cnt, c + n - _next + min(c, n-_next))

    answer += side_cnt
    return answer

