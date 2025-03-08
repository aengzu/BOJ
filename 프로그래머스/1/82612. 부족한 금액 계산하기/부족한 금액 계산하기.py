def solution(price, money, count):
    cost = 0
    for i in range(1, count+1):
        cost += price * i
    return 0 if money - cost > 0 else cost - money 