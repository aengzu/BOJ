r, c, zr, zc = list(map(int, input().split()))

lst = [
    input() for _ in range(r)
]

for i in range(r):
    tmp = ''
    for j in range(c):
        tmp += lst[i][j]*zc
        print(lst[i][j]*zc, end='')
    print()
    for k in range(1, zr):
        print(tmp)
