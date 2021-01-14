# 올바른 문자열인지 확인
def isright(p):
    s = []
    try:
        for i in p:
            if i == '(':
                s.append('(')
            else:
                s.pop()
        return True
    except:
        return False

# u,v로 분리하기
def divide(p):
    cnt = [0,0]
    for i in p:
        if i == '(':
            cnt[0] += 1
        else:
            cnt[1] += 1
        if cnt[0] == cnt[1]:
            break
    return p[:sum(cnt)],p[sum(cnt):] 
# 괄호 뒤집기
def reverse(u):
    result = ''
    for i in u:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    answer = ''

    while len(p) != 0:
        u,p = divide(p)
        if isright(u):
            answer += u
        else:
            answer += '(' + solution(p) + ')' + reverse(u[1:-1])
            break
    return answer

# 누군가 엄청나게 짠코드.. 아직이해못하겠다
def solution2(p):
    if p=='': 
        return p
    r=True
    c=0
    for i in range(len(p)):
        if p[i]=='(': 
            c-=1
        else: 
            c+=1
        if c>0: 
            r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
