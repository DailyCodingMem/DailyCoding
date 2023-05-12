def solution(t, p):
    answer = 0
    index = len(t) - len(p)
    for i in range(index+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
            print(t[i:i+len(p)])
    return answer