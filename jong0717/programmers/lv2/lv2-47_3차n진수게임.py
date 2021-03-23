# 10진법을 n진법으로 바꾸는 함수
def convert(n,base):
    T = '0123456789ABCDEF'
    q, r = divmod(n,base)
    if q == 0:
        return T[r]
    else:
        return convert(q,base) + T[r]

def solution(n, t, m, p):
    answer = ''
    # n진법으로 변환된 값들을 뜯어서 저장할 리스트
    n_th = []
    # t*m을 초과할일이 없으므로 t*m까지 range
    for i in range(t*m):
        # n진법으로 변환
        conv = convert(i,n)
        # 변환된 값들을 끊어서 길이 1씩 n_th에 추가
        for c in conv:
            n_th.append(c)
    # p=1인게 먼저 하는 거니까 인덱스 -1 해주고 간격이 사람수인 m만큼이니까 m간격으로 접근
    for j in range(p-1,t*m,m):
        answer += n_th[j]
    return answer

