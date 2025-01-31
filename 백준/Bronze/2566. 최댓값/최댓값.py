grids = [
    list(map(int, input().split()))
    for _ in range(9)
]
max_value = -float('inf')
max_row, max_col = -1, -1

for i, row in enumerate(grids):
    for j, num in enumerate(row):
        if num > max_value:
            max_value = num
            max_row, max_col = i, j

print(max_value)
print(max_row+1, max_col+1)