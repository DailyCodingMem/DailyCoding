gwalho = list(input())
def confirm(list):
    stack = []
    if gwalho[0] == ')':
        return False
    for g in gwalho:
        if g == ')':
            if not len(stack):
                return False
            else:
                stack.pop()
        else:
            stack.append(g)
    if len(stack):
        return False
    return True

if confirm(gwalho):
    print("good")
else:
    print("bad")
