birth, n = input().split()
if int(n) == 1 or int(n) == 2:
    age = 112 - int(birth[0:2]) + 1
else:
    age = 12 - int(birth[0:2]) + 1
print(age)