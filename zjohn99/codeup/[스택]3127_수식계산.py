# codeup - 스택 - 수식계산 (2020-09-22)
# https://codeup.kr/problem.php?id=3127

from collections import deque
import sys
sys.stdin = open("codeup/[스택]3127_수식계산.txt",'r')

T = int(input())
for _ in range(T):
    s = deque(input().split())
    method = ['*','+','-']
    first = True
    val = 0
    st = []
    while(s) :
        tmp = s.popleft()
        if tmp in method :
            if tmp == '*' :
                val = st.pop() * st.pop()
            elif tmp == '+' :
                val = st.pop() + st.pop()
            else :
                val = -st.pop() + st.pop()
                
            st.append(val)
        else :
            st.append(int(tmp))
    print(st[0])