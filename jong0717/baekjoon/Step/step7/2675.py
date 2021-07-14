T = int(input())
for _ in range(T):
    result = ''
    r, s = map(str, input().split(' '))
    for i in s:
        result += i*int(r)
    print(result)