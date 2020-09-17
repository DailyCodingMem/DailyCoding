T = int(input())
for test_case in range(T):
    a = input()
    n = len(a)
    print('..#.' * n+ '.')
    print('.#' * n * 2+ '.')
    for i in range(n):
        print('#.'+a[i]+'.', end='')
    print('#')
    print('.#' * n * 2+ '.')
    print('..#.' * n+ '.')