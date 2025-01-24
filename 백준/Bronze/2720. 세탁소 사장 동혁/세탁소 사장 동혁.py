t = int(input())

for _ in range(t):
    c = int(input())
    q, d, n, p = 0, 0, 0, 0
    if c >= 25:
        q = c // 25
        c = c % 25
    if c >= 10:
        d = c // 10
        c = c % 10
    if c >= 5:
        n = c // 5
        c = c % 5
    p = c

    print(q, d, n, p, end= ' ')