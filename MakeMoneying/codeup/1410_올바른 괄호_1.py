String = input()
Start = 0
End = 0
for i in String:
    if i=="(":
        Start += 1
    elif i==")":
        End += 1
print("{} {}".format(Start,End))