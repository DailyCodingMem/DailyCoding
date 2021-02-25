vi = [True]*10
vi[4]=False
print(all(vi)==True)
print(any(vi)==True)
vi = [False]*10
vi[3] = True
print((not any(vi)))
print((any(vi)))