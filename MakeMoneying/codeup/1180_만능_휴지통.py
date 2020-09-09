N = input()
if int(N)<10:
    N = '0'+N
Answer = ((int(N[1])*10 + int(N[0]))*2)%100
print(Answer)
if Answer<=50:
    print("GOOD")
else:
    print("OH MY GOD")