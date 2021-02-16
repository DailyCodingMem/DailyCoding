def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            # 예외처리 : if가 먼저 실행이 되서 '('가 들어가면 pop이 된다.
            try:
                stack.pop()
            # pop이 안되는 경우라면 s[0]이 ')'인 경우밖에없음.
            except:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


