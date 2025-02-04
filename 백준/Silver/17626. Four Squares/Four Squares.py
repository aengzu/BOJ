# 모든 자연수는 넷 또는 그 이하의 제곱수의 합
import math
# --------------
# dp[1] = 1
# dp[2] = 2 = 1 + 1 (dp[1] + 1)
# dt[3] = 3 = 1 + 1 + 1 (dp[2] + 1)
# --------------
# dp[4] = 1 = 2*2 (min(dp[3]+1, 2*2))
# dp[5] = 2 = 2*2 + 1 (
# dp[6] = 3 = 2*2 + 1 + 1
# dp[7] = 4 = 2*2 + 1 + 1 + 1
# dp[8] = 2 = 2*2 + 2*2
# ----------------
# dp[9] = 1 = 3*3
# dp[10] = 2 = 3*3 + 1
# dp[11] = 3 = 3*3 + 1 + 1
# dp[12] = 4 = 3*3 + 1 + 1 + 1
# dp[13] = 2 = 3*3 + 2*2
# dp[14] = 3 = 3*3 + 2*2 + 1
# dp[15] = 4 = 3*3 + 2*2 + 1 + 1
# ----------------
# dp[16] = 1 = 4*4

def calculate_squares(n):
    # case 1) n이 제곱수인 경우 1
    if int(math.sqrt(n)) ** 2 == n:
        return 1

    # case 2) n = a² + b² 인 경우 a 에서 제곱수 뺀게 제곱수일 경우 2
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i * i)) ** 2 == (n - i * i):
            return 2

    # 3. n 이 세 제곱수의 합일 경우 (n - x^2 - y^2이 제곱수이면 3 반환) / n = a² + b² + c²
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i * i)) + 1):
            if int(math.sqrt(n - i * i - j * j)) ** 2 == (n - i * i - j * j):
                return 3

    # 4. 위 모든 경우에 해당하지 않으면 반드시 4개
    return 4

n = int(input())
print(calculate_squares(n))