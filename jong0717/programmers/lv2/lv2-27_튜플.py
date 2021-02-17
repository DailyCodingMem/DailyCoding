def solution(s):
    answer = []
    # s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    # s 잘라서 리스트 만드는게 제일 어려웠다..
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key = len)
    for i in s:
        num = i.split(',')
        for j in num:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


