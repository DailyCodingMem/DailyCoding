A,B = map(int,input().split())
A //= 10000
if B<3:
    Answer = (100-A) + 12
else:
    Answer = 12-A
print(Answer+1)