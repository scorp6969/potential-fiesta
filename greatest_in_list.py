lists = [3, 2, 4, 8, 6, 5, 10]
max_num = lists[0]

for number in lists:
    if number > max_num:
        max_num = number

print(f'Max num : {max_num}')

# print(max(lists))
