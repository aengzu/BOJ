n = int(input())

i = 666
cnt = 0
while True:
    if str(i).__contains__('666'):
        cnt += 1
    if cnt == n:
        print(i)
        break
    i += 1
