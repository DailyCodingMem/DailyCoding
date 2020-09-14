n = int(input())
A = 0
while (n//2+1)-A:
    print("{}{}".format(' '*(n//2-A),'*'*(2*A+1)))
    A += 1