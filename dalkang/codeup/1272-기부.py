john, bob = map(int, input().split(' '))
order = []
end = bob
start = john
if john > bob:
    end = john
    start = bob

for i in range(1, end):
    order.append(i)
    order.append(i*10)

print(order[start-1] + order[end-1])gt