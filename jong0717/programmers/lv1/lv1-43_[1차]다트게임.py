def solution(dartResult):
    n = ''
    s = []
    dartlist = list(dartResult)
    plus_alpha = ['S','D','T','*','#']
    for dart in dartlist:
        if dart not in plus_alpha:
            n += dart
        elif dart == 'S':
            s.append(int(n))
            n = ''
        elif dart == 'D':
            s.append(int(n)**2)
            n = ''
        elif dart == 'T':
            s.append(int(n)**3)
            n = ''
        elif dart == '*':
            if len(s) > 1:
                s[-2] *= 2
            s[-1] *= 2
        elif dart == '#':
            s[-1] *= -1
    return sum(s)

dartResult = "1S2D*3T"
dartlist = list(dartResult)
s = []
n = ''
plus_alpha = ['S','D','T','*','#']
print(dartlist)
for dart in dartlist:
    if dart not in plus_alpha:
        n += dart
    elif dart == 'S':
        s.append(int(n))
        n = ''
    elif dart == 'D':
        s.append(int(n)**2)
        n = ''
    elif dart == 'T':
        s.append(int(n)**3)
        n = ''
    elif dart == '*':
        if len(s) > 1:
            s[-2] *= 2
        s[-1] *= 2
    elif dart == '#':
        s[-1] *= -1

print(sum(s))



