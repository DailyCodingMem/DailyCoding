from itertools import permutations as pmt
def calculation(left,right,mathex):
    if mathex == '+':
        result = int(left) + int(right)
    elif mathex == '-':
        result = int(left) - int(right)
    elif mathex == '*':
        result = int(left) * int(right)
    return result

def solution(expression):
    cals = ["+","-","*"]
    perms = list(pmt(cals,3))
    mathBasket = []
    exBasket = []
    myDigit = ''
    answer = 0
    for i in range(len(expression)):
        if i == len(expression) - 1:
            myDigit += expression[i]
            myDigit = int(myDigit)
            mathBasket.append(myDigit)
        elif expression[i].isdigit():
            myDigit += expression[i]
        else:
            myDigit = int(myDigit)
            mathBasket.append(myDigit)
            myDigit = ''
            exBasket.append(expression[i])
    for i in range(6):
        cal = perms[i]
        myExpress = exBasket[:]
        myMath = mathBasket[:]
        for j in range(3):
            mathEx = cal[j]
            while myExpress and mathEx in myExpress:
                idx = myExpress.index(mathEx)
                A = myMath.pop(idx)
                B = myMath.pop(idx)
                C = myExpress.pop(idx)
                result = calculation(A,B,C)
                myMath.insert(idx, result)
        if answer < abs(myMath[0]):
            answer = abs(myMath[0])
    return answer


# 다른사람 풀이..
def solution2(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            print(temp)
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
