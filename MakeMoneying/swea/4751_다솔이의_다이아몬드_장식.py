import sys
sys.stdin = open("4751in.txt",'r')

T = int(input())
for Count in range(T):
    Input = input()
    if len(Input)==1:
        print('..#..')
        print('.#.#.')
        print('#.{}.#'.format(Input))
        print('.#.#.')
        print('..#..')
    else:
        N = len(Input)
        print('..#.'*N + '.')
        print('.#.#'*N + '.')
        for i in range(N):
            print('#.{}.'.format(Input[i]),end='')
        print('#')
        print('.#.#'*N + '.')
        print('..#.'*N + '.')