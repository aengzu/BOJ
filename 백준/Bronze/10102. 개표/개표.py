v = int(input())

votes = input()
a, b = 0, 0

for i in range(v):
    match votes[i]:
        case 'A':
            a += 1
        case 'B':
            b += 1


if a>b:
    print('A')
elif a<b:
    print('B')
else:
    print('Tie')