h, k, d = map(str,input().split())
for i in range(int(h)):
    if d == 'L':
        print(' '*i+'*'*int(k))
    else:
        print(' '*(int(h)-i-1)+'*'*int(k))