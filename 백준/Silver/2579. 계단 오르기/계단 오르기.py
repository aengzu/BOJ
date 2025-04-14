n = int(input())

stair_score = [
    int(input())
    for _ in range(n)
]

now_score = [[(0, 0), (0, 0)] for _ in range(n)]

# 1번째 계단 (10, 1)
# 2번째 계단 30 (30, 2)
# 3번째 25 (25, 1)
# 4번째 55, 50 (55, 1), (50, 2)
# 5번째 65, 35 (35, 1), (65, 2)
# 6번째 (55, 2), (75, 1)

# 첫번째 계단
now_score[0][0] = (stair_score[0], 1)
# 두번째 계단
if n >= 2:
    now_score[1][0] = (stair_score[1] + stair_score[0], 2)
    now_score[1][1] = (stair_score[1], 1)

for i in range(2, n):
    now_stair = stair_score[i]

    # i-2 에서 올때
    max_pprev = max(now_score[i-2], key=lambda x: x[0])[0]
    now_score[i][0] = (max_pprev + now_stair, 1)

    # i-1 에서 올때
    if now_score[i - 1][0][1] != 2:
        now_score[i][1] = (now_score[i - 1][0][0] + now_stair, 2)
    else:
        now_score[i][1] = (now_score[i - 1][1][0] + now_stair, 2)

print(max(now_score[n-1], key=lambda x: x[0])[0])
