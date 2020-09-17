a,b = map(float,input().split())
answer = max(a+b, a-b,b-a,a*b,a/b,b/a,a**b,b**a)
print('%.6f' % answer)