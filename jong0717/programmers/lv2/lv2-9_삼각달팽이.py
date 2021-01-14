def solution(n):
    arr = [[0]*n for _ in range(n)]
    num = 1
    x,y = -1, 0
    result = []
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                result.append(arr[i][j])
    return result

n = 4
# result = []
# answer = [[1],[2,9],[3,10,8],[4,5,6]]
# answer[3].append(7)

# print(answer)
# print(len(answer[3]))

print(result)