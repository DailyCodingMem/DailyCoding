# codeup - 스택 - 올바른괄호2 (2020-09-23)
# https://codeup.kr/problem.php?id=3129

import sys
sys.stdin = open("codeup/[스택]3130_올바른괄호2.txt",'r')


def solution():
    if s.count('(') == s.count(')') :
        st = []
        st.append(s[0])

        if st[0] == ')' :
            return 'bad'
        else :
            for i in range(1, len(s)) :
                if s[i] == '(' :
                    st.append('(')
                else :
                    if st :
                        st.pop()
                    else :
                        return 'bad'
            else :
                if st :
                    return 'bad'
                else :
                    return 'good'
    else :
        return 'bad'

    


T = int(input())
for _ in range(T):
    s = input()
    print(solution())
