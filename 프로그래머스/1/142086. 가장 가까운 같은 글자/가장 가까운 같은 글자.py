def solution(s):
    alpha = [-1] * 26
    answer = []
    for idx, c in enumerate(s):
        if alpha[ord(c) - 97] == -1:
            answer.append(-1)
        else:
            answer.append(idx-alpha[ord(c)-97])
        alpha[ord(c) - 97] = idx
    return answer