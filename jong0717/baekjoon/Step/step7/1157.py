words = input().upper()
simple_words = list(set(words))
cnt_list = []
for i in simple_words:
    cnt_list.append(words.count(i))
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_idx = cnt_list.index(max(cnt_list))
    print(simple_words[max_idx])