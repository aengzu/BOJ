n = int(input())
ans_s = 0
ans = 0

for _ in range(n):
    person = list(map(int, input().split()))
    l = len(person)
    s = 0
    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                s = max(s, (person[i] + person[j] + person[k]) % 10)
                ans_s = max(ans_s, s)
                if ans_s == s:
                    ans = _ + 1


print(ans)