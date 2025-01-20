n = int(input())

for i in range(n):
    r, e, c = list(map(int, input().split()))
    a_cost = e - c
    na_cost = r

    if a_cost > na_cost:
        print("advertise")
    elif a_cost < na_cost:
        print("do not advertise")
    else:
        print("does not matter")