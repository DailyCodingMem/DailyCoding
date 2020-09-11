x, y = map(int, input().split())
print('%f' % max(x+y, x-y, y-x, x*y, x/y, y/x, x**y, y**x))