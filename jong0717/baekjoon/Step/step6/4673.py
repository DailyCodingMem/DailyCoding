all_nums = set(range(1,10001))
generate_nums = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generate_nums.add(i)
self_num = sorted(all_nums - generate_nums)
for i in self_num:
    print(i)


