phone = input('Phone No : ')
output = ''
digits_map = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five'
}

for ch in phone:
    output += digits_map.get(ch, '!') + ' '

print(output)
