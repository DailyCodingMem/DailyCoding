def solution(n, lost, reserve):
    answer = 0
    return answer
n = 3
answer = 0
lost = [3]
reserve = [1]
able_class = n - len(lost)
plus_res = [i + 1 for i in reserve]    
minus_res = [i -1 for i in reserve]
for ls in lost:
    if ls in minus_res:
        able_class += 1
    
print(able_class)