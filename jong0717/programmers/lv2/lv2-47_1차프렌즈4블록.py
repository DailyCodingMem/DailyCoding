def convert(n,base):
    T = '0123456789ABCDEF'
    q, r = divmod(n,base)
    if q == 0:
        return T[r]
    else:
        return convert(q,base) + T[r]

def solution(n, t, m, p):
    answer = ''
    return answer

m = 2
n = 2
t = 4
p = 1
answer = ''
n_th = []
for i in range(t*m):
    conv = convert(i,n)
    for c in conv:
        n_th.append(c)
print(n_th)
for j in range(p-1,t*m,m):
    answer += n_th[j]
print(answer)