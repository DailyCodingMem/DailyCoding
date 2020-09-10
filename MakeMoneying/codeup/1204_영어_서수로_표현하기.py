n = int(input())
dec = n%10
if n//10==1:
    print("{}th".format(n))

else:
    if dec==1:
        print("{}st".format(n))
    elif dec==2:
        print("{}nd".format(n))
    elif dec==3:
        print("{}rd".format(n))
    else:
        print("{}th".format(n))
