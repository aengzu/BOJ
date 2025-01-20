odd_sum = 0
min_odd = 101

for i in range(7):
    n = int(input())
    if n % 2 != 0:
        odd_sum += n
        min_odd = min(min_odd, n)

if odd_sum == 0:
    print(-1)
else:
    print(odd_sum)
    print(min_odd)
