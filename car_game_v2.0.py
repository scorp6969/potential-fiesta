command = ''
is_started = False

while True:
    command = input('> ').lower()

    if command == 'quit':
        break

    elif command == 'start':
        if is_started:
            print('Car is already started...')
        else:
            is_started = True
            print('Car started...')

    elif command == 'stop':
        if not is_started:
            print('Car is already stopped')
        else:
            is_started = False
            print('Car stopped...')

    elif command == 'help':
        print('''
start - to start a car
stop - to stop a car
quit - to quit the game
        ''')

    else:
        print('Sorry! I don\'t understand.')
