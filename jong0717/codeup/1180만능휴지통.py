#202020909
trash = int(input())
ten = trash // 10
one = trash % 10
n_trash = (one*10 + ten)*2
if n_trash > 100:
    n_trash = n_trash - 100
    if n_trash <= 50:
        print(n_trash)
        print('GOOD')
    elif 50<= n_trash < 100:
        print(n_trash)
        print('OH MY GOD')
else:
    if n_trash <= 50:
        print(n_trash)
        print('GOOD')
    elif 50<= n_trash < 100:
        print(n_trash)
        print('OH MY GOD')

