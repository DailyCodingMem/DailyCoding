N = int(input())
number = [int(bin(x)[2:]) for x in range(2**N)]

# print(number)
for num in number:
    if num % N == 0 and str(num)[:1]=='1':
        print(num)
        break
        


# for num in not_num:
#     if str(num) not in check and check[:1] == '1':
#         print(str(num))
# print('2' in '111')