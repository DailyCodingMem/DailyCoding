def solution(d, budget):
    answer = 0
    d.sort()
    for money in d:
        budget -= money
        if budget >= 0 :
            answer += 1
        else:
            break
    return answer

def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
