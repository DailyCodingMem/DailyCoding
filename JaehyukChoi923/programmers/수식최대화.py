import re
from itertools import permutations
expression = "100-200*300-500+20"
# p = re.compile("\D")
# operators = p.findall(expression)
operators = set(re.findall("\D", expression)) # 패턴: 숫자가 아닌 거, 표현식에서 찾아라. 그리고 중복 제거.
priors = permutations(operators) # 위에서 찾은 연산자를 순열로. 연산자 우선순위.
candi = []
for prior in priors: # 각각의 우선순위에 대해서 봐 볼거야
    temp = re.compile("(\D)").split(expression) # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
    for operator in prior: # 해당 우선순위에서 연산자 각각 돌면서
        while operator in temp: # 이 연산자가 지금 식 안에 있는 동안
            idx = temp.index(operator)
            temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
    candi.append(abs(int(temp[0])))
print(max(candi))

# p = re.compile("\D")
# m = p.search("123")
# print(m)
