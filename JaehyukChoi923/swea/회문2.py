for _ in range(10):
    tc = int(input())
    arr = []
    for _ in range(100):
        arr.append(input())
    Max = 0
    for i in range(100):
        for j in range(100):
            temp = ''
            for p in range(j, 100):
                temp += arr[i][p]
                if temp == temp[::-1]:
                    if len(temp) > Max:
                        Max = len(temp)

    for j in range(100):
        for i in range(100):
            temp = ''
            for p in range(i, 100):
                temp += arr[p][j]
                if temp == temp[::-1]:
                    if len(temp) > Max:
                        Max = len(temp)

    print(Max)