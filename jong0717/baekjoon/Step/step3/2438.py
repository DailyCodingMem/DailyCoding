n = int(input())
for i in range(n):
    print('*'*(i+1))


#2439
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i) + '*' * i)