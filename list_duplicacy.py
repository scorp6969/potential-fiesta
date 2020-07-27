numbers = [5, 2, 2, 3, 8, 9, 5, 4, 6, 3, 1]
uniques = []

print('Original list ->')
print(f'{numbers}\n')

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print('Removing Duplicates ->')
print(f'{uniques}')
