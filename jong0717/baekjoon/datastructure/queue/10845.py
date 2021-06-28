import sys
n = int(input())
queue = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])