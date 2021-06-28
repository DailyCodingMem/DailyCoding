T = int(input())
for _ in range(T):
    my_str = list(input().split(' '))
    for i in my_str:
        print(''.join(i[::-1]), end=" ")
    


