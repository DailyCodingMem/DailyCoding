sentense = input()
up_sent = sentense.upper()
# print(up_sent)
ans = []
for i in range(len(sentense)):
    if sentense[i] == up_sent[i]:
        ans.append(sentense[i].lower())
    else:
        ans.append(sentense[i].upper())
print(''.join(ans))
        