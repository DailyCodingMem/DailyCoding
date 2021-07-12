T = int(input())
for _ in range(T):
    result = 0
    ans = list(input())
    score = 1
    for a in ans:
        if a == 'O':
            result += score
            score += 1
        else:
            score = 1
    print(result)
        