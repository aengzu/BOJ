def convert_3form(ten):
    digits = []
    while ten > 0:
        digits.append(str(ten % 3))
        ten //= 3
    return ''.join(digits)
    
def solution(n):
    answer = int(convert_3form(n), 3)
    return answer