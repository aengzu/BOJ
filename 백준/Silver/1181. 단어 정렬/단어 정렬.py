n = int(input())
input_lst = []

for _ in range(n):
    input_str = input()
    input_lst.append(input_str)

deduplicated_list = list(set(input_lst))
deduplicated_list.sort()
deduplicated_list.sort(key=lambda x: len(x))


for elem in deduplicated_list:
    print(elem)


