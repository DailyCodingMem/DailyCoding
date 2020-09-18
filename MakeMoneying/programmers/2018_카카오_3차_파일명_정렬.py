def solution(files):
    digitBasket = []

    for file in files:
        wordIdx = 0
        while not file[wordIdx].isdigit(): # 숫자가 나올 때 까지 word인덱스 증가
            wordIdx += 1
        head = file[:wordIdx]
        number = ''
        while wordIdx<len(file) and  file[wordIdx].isdigit():
            number += file[wordIdx]
            wordIdx += 1
        tail = file[wordIdx:]
        digitBasket.append((head,number,tail))

    # haed, number로 분류
    digitBasket = sorted(digitBasket, key = lambda x: (x[0].upper(), int(x[1])))

    answer = []
    for i in digitBasket:
        A = i[0]+i[1]+i[2]
        answer.append(A)
    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
files = ["what1","what2","what3","WHAT01","WhaT02"]
print(solution(files))