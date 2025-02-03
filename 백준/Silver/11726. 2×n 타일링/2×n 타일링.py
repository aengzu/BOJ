n = int(input())

mem = [0] * (n+1)
mem[1] = 1

if n >= 2:
    mem[2] = 2
if n >= 3:
    for i in range(3, n+1):
        mem[i] = mem[i-1] + mem[i-2]
        mem[i] = mem[i] % 10007

print(mem[n])
