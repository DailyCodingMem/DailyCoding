N = int(input())
def prime(cnt):
    for i in range(2,cnt):
        for j in range(i,cnt+1,i):
            if j == cnt:
                print("not prime")
                return 
    print("prime")
    return
prime(N)