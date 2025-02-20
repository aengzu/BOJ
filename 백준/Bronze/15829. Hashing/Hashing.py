n = int(input())
input_str = input()

s = 0
for i in range(n):
    tmp = ord(input_str[i]) - 96
    s += tmp * (31**(i))

h = s % 1234567891
print(h)