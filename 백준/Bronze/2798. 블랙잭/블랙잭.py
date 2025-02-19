n, m = tuple(map(int, input().split()))

cards = list(map(int, input().split()))

one, two, three = 0, 0, 0
ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            one = cards[i]
            two = cards[j]
            three = cards[k]
            s = one + two + three
            if s <= m:
                ans = max(s, ans)

print(ans)