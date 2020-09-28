String = input()
left = right = 0
right_is_bigger = False
for i in String:
    if i=="(":
        left += 1

    elif i==")":
        right += 1

    if right>left:
        right_is_bigger = True

if left==right:
    if right_is_bigger:
        print('bad')

    else: 
        print('good')
else:
    print('bad')