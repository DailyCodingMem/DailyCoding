start, end = input().split()

a = int(start)
b = int(end)
result = []
k = ''
stack = []
for i in range(a, b+1):
    if i%2:
        i = +i
        if len(k)==0:
            k+= str(i)
        else:
            k += '+'+str(i)
        result.append(i)
    else:
        k += '-'+str(i)
        i = -i
        result.append(i)
print('{}={}'.format(k, sum(result)))