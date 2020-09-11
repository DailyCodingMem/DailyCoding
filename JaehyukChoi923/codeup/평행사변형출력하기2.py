h, k, d = input().split()
if d == 'L':
    for i in range(int(h)):
        print(' '*i, end='')
        print('*'*int(k))
else:
    for i in range(int(h)-1, -1, -1):
        print(' ' * i, end='')
        print('*' * int(k))