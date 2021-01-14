def solution(progresses, speeds):
    answer = []
    cnt = 1
    day = (100-progresses[0]) // speeds[0]
    for i in range(1,len(speeds)):
        day1 = (100 - progresses[i]) // speeds[i]
        if day > day1:
            cnt += 1
            print(cnt)
        else:
            answer.append(cnt)
            cnt = 1
    return answer

p = 30
s = 30
print((p-100)//s)
a = "011"
print(int(a))