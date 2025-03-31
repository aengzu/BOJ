import sys

m = int(sys.stdin.readline().rstrip())
s = set()
ans = []

for _ in range(m):
    cmd = sys.stdin.readline().split()

    c = cmd[0]
    if len(cmd) == 1:
        if c == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        x = int(cmd[1])
        if c == 'add':
            s.add(x)
        elif c == 'remove':
            s.discard(x)
        elif c == 'check':
            print('1' if x in s else '0')
        elif c == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
