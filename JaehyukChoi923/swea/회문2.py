for _ in range(1):
    tc = int(input())
    arr = []
    for _ in range(100):
        arr.append(input())
    Max = 0
    for i in range(100): # 행을 잡아주고
        for j in range(100): # 행의 시작점(열)을 잡아줘
            for p in range(j+1, 100):
                temp = arr[i][j:p]
                if temp == temp[::-1]:
                    if len(temp) > Max:
                        Max = len(temp)

    for j in range(100): # 열을 잡아주고
        for i in range(100): # 열의 시작점(행)을 잡아줘
            for p in range(i+1, 100): # 어디까지 갈지
                temp = ''
                temp_range = list(range(p))
                for q in temp_range:
                    temp += arr[q][j]
                    if temp == temp[::-1]:
                        if len(temp) > Max:
                            Max = len(temp)

    print(Max)