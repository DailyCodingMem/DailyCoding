import sys
T = int(input())
for tc in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{tc+1}: {a} + {b} = {a+b}")