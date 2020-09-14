h, m = map(int, input().split())
if h == 0:
    h = 24
if m >= 30:
    m -= 30
else:
    m += 60
    m -= 30
    h -= 1
if h == 24:
    h = 0
print(h, m)