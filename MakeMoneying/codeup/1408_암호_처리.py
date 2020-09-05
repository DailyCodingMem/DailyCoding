String = input()
ASC = ''
ASC2 = ''
for i in String:
    ASC += chr(ord(i)+2)
    ASC2 += chr((ord(i)*7)%80 +48)
print(ASC)
print(ASC2)