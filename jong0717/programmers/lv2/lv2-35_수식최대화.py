from itertools import permutations as pmt
def solution(expression):
    cals = ["+","-","*"]
    perms = pmt(cals,3)
    stack = list(expression)

    answer = 0
    return answer
expression = "100-200*300-500+20"
cals = ["+","-","*"]
# stack = list(expression.split())
perms = list(pmt(cals,3))
for perm in perms:
    print(perm[2])
    print(expression.split('perm[2]'))
    
# print()
print(perms)
print(eval(expression))