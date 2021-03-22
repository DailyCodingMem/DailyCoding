from string import ascii_uppercase
def solution(msg):
    answer = []
    alpha = list(ascii_uppercase)
    leng = 0
    idx = 0

    while True:
        leng += 1
        # print(msg[idx:idx+leng])
        if not msg[idx:idx+leng] in alpha:
            alpha.append(msg[idx:idx+leng])
            # print(alpha)
            answer.append(alpha.index(msg[idx:idx+leng-1]) + 1)
            # print(answer)
            # alpha.index(msg[idx:idx+leng])
            idx = idx + leng - 1
            leng = 0
        else:
            if idx+leng-1 == len(msg):
                # print(msg[idx:idx+leng-1])
                answer.append(alpha.index(msg[idx:idx+leng-1]) + 1)
                break
    return answer



msg = 'KAKAO'
answer = []
alpha = list(ascii_uppercase)
leng = 0
idx = 0

while True:
    leng += 1
    # print(msg[idx:idx+leng])
    if not msg[idx:idx+leng] in alpha:
        alpha.append(msg[idx:idx+leng])
        # print(alpha)
        answer.append(alpha.index(msg[idx:idx+leng-1]) + 1)
        # print(answer)
        # alpha.index(msg[idx:idx+leng])
        idx = idx + leng - 1
        leng = 0
    else:
        if idx+leng-1 == len(msg):
            # print(msg[idx:idx+leng-1])
            answer.append(alpha.index(msg[idx:idx+leng-1]) + 1)
            break
print(answer)