t = int(input())


for j in range(t):
    y_sum, k_sum = 0, 0
    for i in range(9):
        Y, K = tuple(map(int, input().split()))
        y_sum += Y
        k_sum += K

    if y_sum > k_sum:
        print("Yonsei")
    elif y_sum < k_sum:
        print("Korea")
    else:
        print("Draw")