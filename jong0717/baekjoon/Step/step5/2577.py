a = int(input())
b = int(input())
c = int(input())
multiple = str(a * b * c)
for i in range(10):
    print(multiple.count(str(i)))
