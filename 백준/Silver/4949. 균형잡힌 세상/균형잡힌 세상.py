push_trigger = ('(', '[')
pop_trigger = (')', ']')

while True:
    input_str = input()
    if input_str == '.':
        break
    parentheses = []
    ans = True
    for i in range(len(input_str)):
        if input_str[i] in push_trigger:
            parentheses.append(input_str[i])
            continue
        if input_str[i] in pop_trigger:
            if len(parentheses) == 0:
                ans = False
                continue
            tmp = parentheses.pop()
            if tmp != push_trigger[pop_trigger.index(input_str[i])]:
                ans = False
    if len(parentheses)!=0:
        ans = False
    print('yes') if ans else print('no')

