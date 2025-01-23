a, b, c, d, e, f = list(map(int, input().split()))

x = (c*e - b*f) / (a*e - b*d)
y = (d*c - a*f) / (b*d - a*e)

print(int(x), int(y))