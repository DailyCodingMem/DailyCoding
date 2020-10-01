#20200910
N = int(input())
num_str = ''
M = str(N)
if 4 <= N % 10 <= 10 or N % 10 == 0:
    num_str = M + 'th'
elif 11 <= N <= 13:
    num_str = M + 'th'
else:
    if N % 10 == 1:
        num_str = M + 'st'
    elif N % 10 == 2:
        num_str = M + 'nd'
    else:
        num_str = M + 'rd'
print(num_str)