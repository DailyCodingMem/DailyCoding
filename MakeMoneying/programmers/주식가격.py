def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        count = 0
        for j in range(i+1,len(prices)):
            count += 1
            if prices[i]>prices[j]:
                answer[i] = count
                break
        else:
            answer[i] = count
    # print(answer)
    return answer



prices = [1, 2, 3, 2, 3]
solution(prices)