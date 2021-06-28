ls = list(input())
rs = []
T = int(input())
for _ in range(T):
    cmd = tuple(input().split(' '))
    if cmd[0] == 'L':
        if ls:
            rs.append(ls.pop())
    elif cmd[0] == 'D':
        if rs:
            ls.append(rs.pop())
    elif cmd[0] == 'B':
        if ls:
            ls.pop()
    else:
        ls.append(cmd[1])
print(''.join(ls+rs[::-1]))