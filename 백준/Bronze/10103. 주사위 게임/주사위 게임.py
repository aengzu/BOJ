n = int(input())
s_sum, c_sum = 0, 0
for i in range(n):
    c, s = tuple(map(int, input().split()))
    if s<c:
        # c wins
        s_sum -= c
    elif c<s:
        c_sum -= s

print(100+c_sum)
print(100+s_sum)