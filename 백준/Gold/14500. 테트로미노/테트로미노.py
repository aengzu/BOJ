from collections import deque

n, m = tuple(map(int, input().split()))

board = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 상 하 좌 우
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

q = deque()
max_sum = 0
ans = []

shapes = [
    # -
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # |
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    # ㅁ
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # L자
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 2), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    # Z자
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    # ㅗ, ㅜ, ㅓ, ㅏ
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(0, 1), (1, 0), (1, 1), (2, 1)],  # ㅓ
    [(0, 1), (1, 0), (1, 1), (1, 2)],  # ㅗ
    [(0, 0), (1, 0), (1, 1), (2, 0)]   # ㅏ
]


for i in range(n):
    for j in range(m):
        for sh in shapes:
            s = 0
            is_possible = True
            for dx, dy in sh:
                nx = j + dx
                ny = i + dy
                if 0 <= nx < m and 0 <= ny < n:
                    s += board[ny][nx]
                else:
                    is_possible = False
                    break
            if is_possible:
                max_sum = max(max_sum, s)

print(max_sum)