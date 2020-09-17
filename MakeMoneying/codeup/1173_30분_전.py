A,B = map(int,input().split())
if B>=30:
    B -= 30
else:
    B += 30
    A -= 1
if A<0:
    A += 24
print("{} {}".format(A,B))