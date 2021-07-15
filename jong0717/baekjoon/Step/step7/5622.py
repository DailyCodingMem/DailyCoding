dial = ['ABC', 'DEF', 'GHI','JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
memory = input()
result = 0
for i in range(len(memory)):
    for j in dial:
        if memory[i] in j:
            result += dial.index(j) + 3
print(result)