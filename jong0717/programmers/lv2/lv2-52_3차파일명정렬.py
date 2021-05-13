def solution2(files):
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


# 정규표현식 이용
import re
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 1
temp = [re.split(r"([0-9+])",s) for s in files]
print(temp)
# 2
sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
#
a = "img12.png"
print(re.split(r"([0-9])",a))
