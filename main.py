import random
print('''
    Syres RPS game in python.
    nb; type end to stop game when tired
''')
while True:

    comp_choice = random.choice(['rock', 'paper', 'scissors'])

    print('Rock, paper or Scissors?')
    user_choice = input(':::: ')

    if user_choice != 'rock':
        if user_choice != 'paper':
            if user_choice != 'scissors':
                if user_choice == 'end':
                    print('You have ended Syres game.')
                    break
                else:
                    print('Your choice is not part of the options')
                    break
    else:
        if user_choice == comp_choice:
            print('Its a tie')
        elif user_choice != comp_choice:
            if user_choice == 'rock' and comp_choice == 'paper':
                print('Computer chose: ', comp_choice, '\n', 'You chose: ', user_choice, 'Computer won!!')
            elif user_choice == 'rock' and comp_choice == 'scissors':
                print('Computer chose: ', comp_choice, '\n', 'You chose: ', user_choice, 'You won!!')
            elif user_choice == 'paper' and comp_choice == 'rock':
                print('Computer chose: ', comp_choice, '\n', 'You chose: ', user_choice, 'You won!!')
            elif user_choice == 'scissors' and comp_choice == 'rock':
                print('Computer chose: ', comp_choice, '\n', 'You chose: ', user_choice, 'Computer won!!')
            else:
                break
        else:
            print('invalid choice')
            break

print('thanks for playing')