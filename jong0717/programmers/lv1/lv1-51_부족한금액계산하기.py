def solution(price, money, count):
    result = 0
    for i in range(1,count+1):
        result += i
    if result*price - money > 0:
        return result*price-money
    else:
        return 0

