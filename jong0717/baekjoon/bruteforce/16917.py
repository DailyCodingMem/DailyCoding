A, B, C, X, Y = map(int,input().split())
if A+B < 2*C:
    print(A * X + B * Y)
else:
    res = 2*C*min(X,Y)
    if X >= Y:
        dif = X - Y
        res += min(A * dif, 2*C*dif)
    else:
        dif = Y - X
        res += min(B*dif, 2*C*dif)
    print(res)