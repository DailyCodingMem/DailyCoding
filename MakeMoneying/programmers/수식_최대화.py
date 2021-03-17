def conclusion(left,right,mathex):
    if mathex == "+":
        result=int(left)+int(right)
    elif mathex == "-":
        result=int(left)-int(right)
    elif mathex == "*":
        result=int(left)*int(right)
    return result

def solution(expression):
    mathex = [
        ["*","+","-"],
        ["*","-","+"],
        ["+","-","*"],
        ["+","*","-"],
        ["-","*","+"],
        ["-","+","*"]]
    mathBasket = [] # [100, 200, 300, 500, 20]
    exBasket = [] # ['-', '*', '-', '+']
    myDigit = ""
    answer = 0
    for i in range(len(expression)):
        if i == len(expression)-1:
            myDigit += expression[i]
            myDigit = int(myDigit)
            mathBasket.append(myDigit)
        elif expression[i].isdigit():
            myDigit += expression[i]
        else:
            myDigit = int(myDigit)
            mathBasket.append(myDigit)
            myDigit = ""
            exBasket.append(expression[i])
    for i in range(6):
        mathexpression = mathex[i] # ["*","+","-"]
        myExpress = exBasket[:] # ['-', '*', '-', '+']
        myMath = mathBasket[:] # [100,200,300,500,20]
        for j in range(3):
            mathEx = mathexpression[j] # "*"
            while myExpress and mathEx in myExpress:
                exIndex = myExpress.index(mathEx)
                A = myMath.pop(exIndex)
                B = myMath.pop(exIndex)
                C = myExpress.pop(exIndex)
                result = conclusion(A,B,C)
                myMath.insert(exIndex,result)
        if answer < abs(myMath[0]):
            answer = abs(myMath[0])


    return answer



expression = "50*6-3*2"
expression = "100-200*300-500+20"
print(solution(expression))