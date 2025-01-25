s = 0
sub_num = 0.0
grade_map = {
    'A+':4.5, 'A0': 4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0,
    'D+':1.5, 'D0':1.0, 'F':0.0
}

for _ in range(20):
    sub, score, grade = list(input().split())
    if grade == 'P':
        continue
    s += float(score) * grade_map[grade]
    sub_num += float(score)

print(f'{s/sub_num:.6f}')
