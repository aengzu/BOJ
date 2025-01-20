A, B, C = 300, 60, 10

t = int(input())
a, b, c = 0, 0, 0

if t % 10 != 0:
    print(-1)
else:
    while t>1:
        if t >= A:
            a += t//A
            t = int(t%A)
            continue
        if t>= B:
            b += t//B
            t = int(t%B)
            continue
        if t>=C:
            c += t//C
            t = int(t%C)
            continue
    print(a, b, c, end=' ')