
n = int(input())

members = [ list(input().split()) for _ in range(n)]

members.sort(key = lambda x:int(x[0]))

for elem in members:
    print(elem[0], elem[1])