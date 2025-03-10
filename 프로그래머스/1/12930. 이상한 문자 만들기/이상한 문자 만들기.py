def solution(s):
    answer = ''
    str_lst = s.split(' ')
    new_st = []
    for st in str_lst:
        new_st += [c.upper() if idx % 2 == 0 else c.lower() for idx, c in enumerate(st)]
        print('st: ', st)
        new_st += ' '
        print('new st: ', new_st)
    return ''.join(new_st)[:-1]

        