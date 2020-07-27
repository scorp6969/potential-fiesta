patterns = [5, 2, 5, 2, 2]

# cheat
# for pattern in patterns:
#     print('x' * pattern)

for x_count in patterns:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
