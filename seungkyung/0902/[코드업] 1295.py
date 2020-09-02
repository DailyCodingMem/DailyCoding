sentense = input()
result = ''

for k in sentense:
    if k.isupper():
        result+= k.lower()
    else:
        result+= k.upper()
print(result)
