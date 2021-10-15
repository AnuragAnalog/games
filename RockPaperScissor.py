import random

wins = {
	('r', 's'),
	('s', 'p'),
	('p', 'r')
}

USER = "user"
COMPUTER = "computer"
TIE = "tie"

def play():
    choice=input('Enter a choice..."r" for Rock,"p" for Paper,"s" for Scissors: ')
    user_choice=choice.lower()
    computer_choice=random.choice(['r','p','s'])

    winner=None
    if(user_choice==computer_choice):
        winner = TIE
    elif (user_choice, computer_choice) in wins :
        winner = USER
    elif (computer_choice, user_choice) in wins :
        winner = COMPUTER

    if winner :
        if winner == TIE :
            print('You are tied with the computer...')
        else :
            print(f"The user chooses {user_choice}, and the computer chooses {computer_choice}. So, the {winner} wins!")
    else:
        print('Something is wrong')

    return winner  

def main():
    _winner = play()

if __name__=='__main__':
    main()
