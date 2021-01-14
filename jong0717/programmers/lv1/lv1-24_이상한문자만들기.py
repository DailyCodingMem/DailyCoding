def solution(s):
    words = s.split(' ')
    print(words)
    answer = []
    for word in words:
        new_s = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_s += word[i].upper()
            else:
                new_s += word[i].lower()
        answer.append(new_s)
    return ' '.join(answer)

print(solution("try hello world"))
