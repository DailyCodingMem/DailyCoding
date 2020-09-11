h,k,d = input().split()
h = int(h)
k = int(k)
if d=='L':
    cnt = 0
    while cnt<h:
        print("{}{}".format(' '*cnt,'*'*k))
        cnt += 1
elif d=='R':
    cnt = h
    while cnt:
        cnt-=1
        print("{}{}".format(' '*cnt,'*'*k))
