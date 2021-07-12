C = int(input())
for _ in range(C):
    scores = list(map(int,input().split(' ')))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for score in scores[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / scores[0] * 100
    print(f'{rate:.3f}%')