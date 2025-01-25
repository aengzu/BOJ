s = input()
s = s.upper()

alph = [0] * 26

for c in s:
    alph[ord(c) - 65] += 1

max_a = 0
max_i = -1
max_cnt = 0
for i in range(len(alph)):
    if max_a == alph[i]:
        max_cnt += 1
        max_i = i
    elif max_a < alph[i]:
        max_a = alph[i]
        max_cnt = 0
        max_i = i

if max_cnt >= 1:
    print('?')
else:
    print(chr(max_i + 65))