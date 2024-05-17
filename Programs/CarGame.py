inputCommand = ''
has_started = False
print("Welcome to Car Game.\n")
while True:
    print("""Please select an action from below: \nstart - to start the car \nstop - to stop the car \nquit - to exit\n""")
    inputCommand = input('Enter an action: ')
    if inputCommand.upper() == 'START':
        if has_started:
            print("Car already started\n")
        else:
            has_started = True
            print("Car started...Ready to go!\n")
    elif inputCommand.upper() == 'STOP':
        if not has_started:
            print("Car already stopped.\n")
        else:
            has_started = False
            print('Car stopped.\n')
    elif inputCommand.upper() == 'HELP':
        print("""start - to start the car \nstop - to stop the car \nquit - to exit\n""")
    elif inputCommand.upper() == 'QUIT':
        break
    else:
        print("I don't understand that.\n")
