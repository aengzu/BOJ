s = input()
map_dialog = {
    'ABC': 2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9, '+-/*%':0
}
dialog = ''
for i in range(len(s)):
    c = s[i]
    for k, v in map_dialog.items():
        if k.__contains__(c):
            dialog += str(v)

ans = 0
for i in range(len(s)):
    ans += int(dialog[i]) + 1

print(ans)