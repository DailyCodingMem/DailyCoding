import sys
sys.stdin = open("1759in.txt",'r')


def password(cnt,word):
    global result
    if len(word) == L:
        result.append(word)
        return

    for i in range(cnt,C):
        if visited[i]:
            visited[i] = False
            password(i+1,word+alpha[i])
            visited[i] = True


L,C = map(int,input().split())
alpha = []
for i in input().split():
    alpha.append(i)
alpha.sort()
visited = list(True for _ in range(C))
result = []
password(0,"")
answer = []
while result:
    word = result.pop(0)
    vowel = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
    if vowel >= 1 and (len(word) - vowel)>=2:
        answer.append(word)
for i in answer:
    print(i)