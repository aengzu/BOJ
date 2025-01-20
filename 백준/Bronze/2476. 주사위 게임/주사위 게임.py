t = int(input())

max_money = 0
for i in range(t):
    dices = list(map(int, input().split()))
    s = set(dices)
    money = 0

    if len(s) == 1:
        money = 10000 + dices[0]*1000
    elif len(s) == 3:
        money = max(dices)*100
    else:
        if dices[0] == dices[1] or dices[0] == dices[-1]:
            money = dices[0]*100 + 1000
        else:
            money = dices[-1]*100 + 1000

    max_money = max(money, max_money)

print(max_money)