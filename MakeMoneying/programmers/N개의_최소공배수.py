def solution(arr):
    Max = max(arr)
    basket = []
    answer = 1
    for i in arr:
        A = i
        divBasket = {}
        for div in range(2,i+1): # div 는 2부터 시작하는 약수
            while not A%div and A!=1: # 정수이면
                if div in divBasket:
                    divBasket[div] += 1
                    A = A//div
                else:
                    divBasket[div] = 1
                    A = A//div
        basket.append(divBasket)
        
    # print(basket) [{2: 1}, {2: 1, 3: 1}, {2: 3}, {2: 1, 7: 1}]
    result = {}
    for i in range(len(basket)):
        for j in basket[i]:
            if j in result:
                result[j] = max(result[j],basket[i][j])
            else:
                result[j] = basket[i][j]
    # print(result) {2: 3, 3: 1, 7: 1}
    for i in result:
        answer *= i**result[i]
    return answer


arr = [2,6,8,14]
print(solution(arr))