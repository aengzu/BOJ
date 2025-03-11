n = int(input())

ranking = [1] * n

big = [
    list(map(int, input().split())) for _ in range(n)
]

for idx, person in enumerate(big):
    for elem in big:
        if person == elem:
            continue
        if person[0] < elem[0] and person[1] < elem[1]:
            ranking[idx] += 1

print(*ranking)