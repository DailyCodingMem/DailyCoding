def solution(s):
    answer = ''
    s_list = list(map(int,s.split()))
    print(s_list)
    print(max(s_list))
    answer = str(min(s_list)) + ' ' + str(max(s_list))
    return answer

s = '-1 -2 -3 -4'
answer = ''
print(answer)