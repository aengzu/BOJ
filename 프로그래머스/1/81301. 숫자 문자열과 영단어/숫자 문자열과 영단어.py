import re

def solution(s):
    answer = ''
    pattern = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    regex_pattern = r'(' + '|'.join(pattern) + r'|\d+)'
    result = re.findall(regex_pattern, s)
    for num in result:
        if num.isdigit():
            answer += num
        else:
            answer += str(pattern.index(num))
    return int(answer)