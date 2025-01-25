croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
ans = 0

for i in croa:
    s = s.replace(i, '*')
print(len(s))