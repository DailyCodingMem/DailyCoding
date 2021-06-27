def solution(code, day, data):
    answer = []
    result = []
    for d in data:
        d_list = d.split(' ')
        if d_list[1].split('=')[1] == code and d_list[2].split('=')[1][:-2] == day:
            time = d_list[2].split('=')[1][-2:]
            price = int(d_list[0].split('=')[1])
            answer.append([time,price])
    answer.sort()
    for i in range(len(answer)):
        result.append(answer[i][1])
    return result

code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
answer = []
result = []
for d in data:
    d_list = d.split(' ')

    if d_list[1].split('=')[1] == code and d_list[2].split('=')[1][:-2] == day:
        time = d_list[2].split('=')[1][-2:]
        price = int(d_list[0].split('=')[1])
        answer.append([time,price])
answer.sort()
for i in range(len(answer)):
    result.append(answer[i][1])
print(result)