n = int(input())

# 1 7

# 1 -> 1개 = 1
# 2 - 7 -> 6개 = 1+1 ~ 1 + 6*(1)
# 8 - 19 -> 12개 = <1 + 6*(1)> + 1 ~ <1 + 6*(1)> + 6*2
# 20 - 37 -> 18개 = (<1 + 6*(1)> + 6*2) + 1 ~ (<1 + 6*(1)> + 6*2) + 6*3

i = 1
prev = 1

while True:
    if n == 1:
        print(1)
        break
    start = prev + 1
    end = prev + 6*i

    if n in range(start, end+1):
        print(i+1)
        break

    prev = end
    i += 1
