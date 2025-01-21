## stdin 을 통해 줄글 입력 받을 수 있다
import sys

inStr = sys.stdin.read()
count_alpha = [0] * 26

for s in inStr:
    if s.islower():
        count_alpha[ord(s) - 97] += 1

for i in range(26):
    if count_alpha[i] == max(count_alpha):
        print(chr(i+97), end='')