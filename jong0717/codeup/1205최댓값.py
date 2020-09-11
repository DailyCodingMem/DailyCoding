n, m = map(int,input().split())
result = [n+m, n-m, m-n, n/m, m/n, n**m, m**n]
print("%0.6f" %float(max(result)))
    