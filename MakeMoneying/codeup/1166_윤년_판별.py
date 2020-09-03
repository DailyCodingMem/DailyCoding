A = int(input())
if not A%400:
    print("yes")
elif not A%100:
    print("no")
elif not A%4:
    print("yes")
else:
    print("no")