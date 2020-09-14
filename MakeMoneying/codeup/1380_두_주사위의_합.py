N = int(input())
if N>6:
    A = 6
    while A and N-A!=7:
        print("{} {}".format(N-A,A))
        A-=1
else:
    A = 1
    while A!=N:
        print("{} {}".format(A,N-A))
        A += 1
