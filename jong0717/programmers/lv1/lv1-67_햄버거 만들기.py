def solution(ingredient):
    answer = 0
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]	
answer = 0
s = []
for i in ingredient:
    s.append(i)

    if s[-4::] == [1,2,3,1]:
        answer += 1
        for h in range(4):
            s.pop()
print(answer)