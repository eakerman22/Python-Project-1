import random
        
def play_again(name):
    play_again = ''
    while play_again != 'yes' and play_again != 'no':
        play_again = input("{}, would you like to play the Number Guessing Game again?  yes/no  ".format(name))
        if play_again.lower() == 'yes':
            print("Ok, great!")
            return True
            new_game()
            break
        elif play_again.lower() == 'no':
            print("Thanks for playing! We hope to see you back soon!")
            return False
            break
        else:
            print("Invalid response. You must specify yes or no.")
            continue
        
def end_game():
    print("Thanks for playing! We hope to see you back soon.")
    
def user_won(name, attempts):
    if attempts == 1:
        print("Congratulations, {} - You got it! It took you {} attempt.".format(name, attempts))
    else:
        print("Congratulations, {} - You got it! It took you {} attempts.".format(name, attempts))
    print("The game has ended. Thanks for playing!")
            
def continue_playing():
    continue_playing = ''
    while continue_playing != 'yes' and continue_playing != 'no':
        continue_playing = input("Would you like to continue playing?  yes/no  ")
        if continue_playing == 'yes':
            print("Ok, great!")
            return True
            break
        elif continue_playing == 'no':
            print("No problem, thanks for playing! We hope to see you back soon!")
            return False
            break
        else:
            print("Invalid response. You must type in yes or no.")
            continue

def guess_attempt(lower, upper, random_number):
    guess = 0
    while guess <= 0:
        try:
            guess = int(input("What number do you think it is?  "))
            while guess <= 0:
                guess = int(input("You must input a whole number greater than zero. Try again:  "))
            print("You have selected {}.".format(guess))
            if guess >= lower and guess <= upper:
                if guess < random_number:
                    print("Your number is lower than than the correct value. Pick a higher number.")
                if guess > random_number:
                    print("Your number is higher than than the correct value. Pick a lower number.")
                return guess
                break
            else:
                print("Remember - The number is between {} and {}. Try again.".format(lower, upper))
                continue
        except ValueError:
            print("You must input a whole number. Try again:  ")
            continue
            
def get_lower():
    lower = 0
    while lower <= 0:
        try:
            lower = int(input("Input the first number of the range. It must be a whole number greater than zero:  "))
            if lower > 0:
                return lower
                break
        except ValueError:
            print("You must input a whole number greater than 0. Use only numerical characters. Try again:  ")
            continue
    
def get_upper(lower):
    upper = 0
    while upper <= lower:
        try:
            upper = int(input("Input the second number of the range. It must be a number greater than the first number you selected:  "))
            if upper > lower:
                return upper
                break
        except Exception:
            print("Your second number input must be greater than your first number input. Try again:  ")
            continue
        except ValueError:
            print("You must input a whole number. Try again:  ")
            continue
             
def welcome():
    name = input("Welcome to the Number Guessing Game! Please tell us your name:  ")
    name = name.capitalize()
    print("Thanks, {}. In order you win, you will have to correctly guess the number I am thinking of within a range that you will be asked to provide.".format(name))
    return name

def start_game():
    active_game = True
    name = welcome()
    high_score = 1
    new_game(active_game, name, high_score)
    
def new_game(active_game, name, high_score):
    print("High Score: {} ".format(high_score))
    lower = get_lower()
    upper = get_upper(lower)
    random_number = random.randint(lower, upper)
    print("Great! You have selected the range of numbers. Your guess must be a number between {} and {}.".format(lower, upper))
    guess = guess_attempt(lower, upper, random_number)
    attempts = 1
    if guess == random_number:
        user_won(name, attempts) 
        active_game = play_again(name)
        if active_game == True:
            new_game(active_game, name, high_score)
    while guess != random_number:
        active_game = continue_playing()
        if active_game == False:
            end_game()
            break
        guess = guess_attempt(lower, upper, random_number)
        attempts += 1
        if guess == random_number:
            user_won(name, attempts) 
            active_game = play_again(name)
            if active_game == True:
                new_game(active_game, name, high_score)
                break

start_game()