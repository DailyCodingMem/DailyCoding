garo = input()
open = 0
close = 0
for i in garo:
    if i == '(': open += 1
    elif i == ')': close += 1
print(open, close)