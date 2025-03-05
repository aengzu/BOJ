
def print_fizzbuzz(num):
    if num % 3== 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3== 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

for idx in range(1, 4):
    s = input()
    if s.isnumeric():
        d = 4 - idx
        target_num = int(s) + d
        print_fizzbuzz(target_num)
        break


