
T = int(input())
for _ in range(T):
    stack = []
    ps = list(input())
    for p in ps:
        if not stack:
            stack.append(p)
        else:
            if p == '(':
                stack.append(p)
            else:
                if stack[-1] == '(':
                    stack.pop()
    if not stack:
        print('YES')
    else:
        print('NO')
    
