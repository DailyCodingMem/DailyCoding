nums = []
confirm = set()
for _ in range(10):
    nums.append(int(input()))
for num in nums:
    confirm.add(num % 42)
print(len(confirm))