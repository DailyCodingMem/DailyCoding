from string import ascii_lowercase
word = input()
alpha_list = list(ascii_lowercase)
alpha_check = [-1] * 26
for i in word:
    if i in alpha_list:
        idx = alpha_list.index(i)
        alpha_check[idx] = word.index(i)
print(*alpha_check)

