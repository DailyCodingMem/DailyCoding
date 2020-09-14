sentence = input()
password = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for i in sentence:
    if i == ' ':
        ans += ' '
    else:
        ans += password[(password.find(i) + 3) % len(password)]

print(ans)
