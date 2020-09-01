def is_correct(s):
    bal = 0
    for c in s:
        if c == '(':
            bal += 1
        else: 
            if bal <= 0:
                return False
            bal -= 1
    if bal:
        return False
    return True

def reverse(s):
    s = s[1:-1]
    ans = ''
    for c in s:
        if c == '(':
            ans += ')'
        else:
            ans += '('
    return ans

            
def split(s):
    if s == '':
        return ''
    balance = 0
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
        if not balance:
            u = s[:i+1]
            v = s[i+1:]
            if is_correct(u):
                return u + split(v)
            else:
                return '(' + split(v) + ')' + reverse(u)
            
            
    
def solution(p):
    ans = split(p)
    return ans
    
    