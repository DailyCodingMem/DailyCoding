a, b  = map(int,input().split())
num = [x for x in range(a,b+1)]
result = 0
process = ''
for n in num:
    if n % 2:
        result += n
        process = process + '+' + str(n)
    else:
        result -= n
        process = process + '-' + str(n)
if int(process[:2]) >= 0:
    process = process[1:]
print('{}={}'.format(process,result))
