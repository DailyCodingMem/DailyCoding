String = input()
Answer = ''
for i in String:
    if ord(i) >=100:
        Answer += chr(ord(i)-3)
    elif ord(i) == 32:
        Answer += ' '
    else:
        Answer += chr(ord(i) +23)
print(Answer)