def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        number_check = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                number_check = True
            elif not number_check:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1]))) # Head 우선, number 차선으로 정렬

    return [''.join(t) for t in answer]


