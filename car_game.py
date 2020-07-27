command = ''

while True:
    command = input('> ').lower()

    if command == 'quit':
        break

    elif command == 'start':
        print('Car started...')

    elif command == 'stop':
        print('Car stopped...')

    elif command == 'help':
        print('''
start - to start a car
stop - to stop a car
quit - to quit the game
        ''')

    else:
        print('Sorry! I don\'t understand.')
