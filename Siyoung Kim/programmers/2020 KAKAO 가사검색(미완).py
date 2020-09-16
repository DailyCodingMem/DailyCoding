from collections import defaultdict

def solution(words, queries):
    answer = []
    wordsdic = defaultdict(list)
    for word in words:
        wordsdic[len(word)].append(word)
    # print(wordsdic)
    
    for query in queries:
        s = 0
        e = len(query)
        if query[-1] == '?':
            for i in range(len(query)-1,-1,-1):
                if ord('a') <= ord(query[i]) <= ord('z'):
                    e = i + 1
                    break
        elif query[0] == '?':
            for i in range(len(query)):
                if ord('a') <= ord(query[i]) <= ord('z'):
                    s = i
                    break
        x = query[s:e]
        cnt = 0
        for word in wordsdic[len(query)]:
            if word[s:e] == x:
                cnt += 1
        answer.append(cnt)
            
    return answer