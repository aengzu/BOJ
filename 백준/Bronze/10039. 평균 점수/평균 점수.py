students = [0, 0, 0, 0, 0]
s = 0

for i in range(5):
    students[i] = int(input())
    if students[i] < 40:
        students[i] = 40
    s += students[i]

print(int(s/5))