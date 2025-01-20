# GCD : 최대 공약수 (여러 공통 약수 중 가장 큰 수)
# LCM : 최소 공배수 (여러 수의 공통 배수 중 가장 작은 수)

import math

t = int(input())

for i in range(t):
    a, b = tuple(map(int, input().split()))
    print(math.lcm(a, b))