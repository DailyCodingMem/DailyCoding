n = input()
if n[-1] == '1':
    back = 'st'
elif n[-1] == '2':
    back = 'nd'
elif n[-1] == '3':
    back = 'rd'
else:
    back = 'th'
if n == '11' or n == '12' or n == '13':
    back = 'th'
print(n+back)