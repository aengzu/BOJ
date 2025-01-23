s = input()
alpha = [-1] * 26

for i in range(len(s)):
    c = s[i]
    if alpha[ord(c) - 97] == -1:
        alpha[ord(c) - 97] = i

for elem in alpha:
    print(elem, end=' ')