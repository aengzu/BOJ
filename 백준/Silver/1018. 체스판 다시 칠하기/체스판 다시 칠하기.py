# 완탐이 될까?
# 10행까지(0-9) 있다면 0-7 / 1-8 / 2-9 로 총 3번 옮겨가면서 가능 10 - 8 + 1
# 13열까지(0-12) 있다면 0-7 / 1-8 / 2-9 / 3- 10/ 4-11 / 5-12 로 총 6번 옮겨가면서 가능
# 일반화하면 n 행 ->  (0, 7] ~ (n - 8, n-1] 까지

# n 행 m 열
n, m = tuple(map(int, input().split()))
checker_board = [
    list(input())
    for _ in range(n)
]

answer = 65

for i in range(n-8+1):
    for j in range(m-8+1):
        fix_cnt = 0
        row_start, col_start = i, j
        start_color = checker_board[row_start][col_start]
        start_idx = (row_start + col_start) % 2
        for r in range(row_start, row_start + 8):
            for c in range(col_start, col_start + 8):
                if (r + c) % 2 == start_idx:
                    if checker_board[r][c] != start_color:
                        fix_cnt += 1

                else:
                    if checker_board[r][c] == start_color:
                        fix_cnt += 1
        if fix_cnt > 32:
            fix_cnt = 64 - fix_cnt
        answer = min(fix_cnt, answer)

print(answer)