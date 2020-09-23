# codeup - 스택 - STL (2020-09-21)
# https://codeup.kr/problem.php?id=3102

import sys
sys.stdin = open("codeup/[스택]3102_STL.txt",'r')

T = int(input())
for _ in range(T):
    N = int(input())
    st = []
    for _ in range(N):
        s = input()
        if 'push' in s :
            l_index = s.index('(')
            r_index = s.index(')')
            s = s[l_index+2:r_index-1]
            st.append(s)           
        elif 'top' in s :
            if len(st) == 0 :
                print(-1)
            else :
                print(st[-1])
        elif 'pop' in s :
            if len(st) == 0 :
                pass
            else:
                st.pop()

        elif 'empty' in s :
            if len(st) == 0 :
                print('true')
            else :
                print('false')
        else:
            print(len(st))


