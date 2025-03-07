import math 

def solution(n):
    answer = -1
    for i in range(1, int(math.sqrt(n))+1):
        if i*i == n:
            answer = (i+1)**2
    return answer