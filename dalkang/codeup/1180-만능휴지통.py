garbage = input()
reversed_garbage = ''.join(reversed(garbage))
result = int(reversed_garbage) * 2
if 100 <= result:
    result = result % 100
if result <= 50:
    print(result)
    print('GOOD')
elif 50 < result:
    print(result)
    print('OH MY GOD')
    