a, b = tuple(input().split())

s_a = int(a[::-1])
s_b = int(b[::-1])

print(max(s_a, s_b))