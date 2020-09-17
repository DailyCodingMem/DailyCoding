from itertools import product
n = int(input())
perms = list(product(range(1, 7), repeat=2))
for perm in perms:
    if sum(perm) == n:
        print(*perm)
