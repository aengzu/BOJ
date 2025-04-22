n, m = tuple(map(int, input().split()))

n_list = list(map(int, input().split()))
sum_list = [0]
now_s = 0

for i in range(n):
    now_s = now_s + n_list[i]
    sum_list.append(now_s)

for _ in range(m):
    s, e = tuple(map(int, input().split()))
    print(sum_list[e] - sum_list[s-1])