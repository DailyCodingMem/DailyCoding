def solution(t, r):
    result = []
    answer = []
    c_list = []
    for i in range(len(t)):
        c_list.append([t[i],r[i]])
    c_list.sort()
    answer.append(c_list.pop(0))
    while c_list:
        cus1 = answer[-1]
        cus2 = c_list.pop(0)
        if cus1[0] == cus2[0]:
            if cus1[1] < cus2[1]:
                cus2[0] += 1
                answer.append(cus2)
            else:
                cus1[0] += 1
                c_list.insert(0,answer.pop())
                answer.append(cus2)
        else:
            answer.append(cus2)
    for i in range(len(answer)):
        result.append(answer[i][1])
    return result

t = [7,6,8,1]
r = [0,1,2,3]
result = []
answer = []
c_list = []
for i in range(len(t)):
    c_list.append([t[i],r[i]])
c_list.sort()
answer.append(c_list.pop(0))
print(c_list)
while c_list:
    cus1 = answer[-1]
    cus2 = c_list.pop(0)
    if cus1[0] == cus2[0]:
        if cus1[1] < cus2[1]:
            cus2[0] += 1
            answer.append(cus2)
        else:
            cus1[0] += 1
            c_list.insert(0,answer.pop())
            answer.append(cus2)
    else:
        answer.append(cus2)
for i in range(len(answer)):
    result.append(answer[i][1])

# print(c_list)
print(result)
            


