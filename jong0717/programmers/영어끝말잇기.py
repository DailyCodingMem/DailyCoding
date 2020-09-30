def solution(n, words):
    answer = [0,0]
    confirm = []
    peoplenum = 0
    for i, word in enumerate(words):
        peoplenum %= n
        if i >= 1:
            if word in confirm or confirm[-1][-1] != word[0]:
                answer = [peoplenum + 1, (i % n) + 1]
                break
        peoplenum += 1
        confirm.append(word)
    return answer
