import numpy
import math
import random
import time

class NUMBER_GUESSING_GAME:
    """ CREATES A NUMBER GUESSING GAME WITH 3 DIFFICULTIES
    """
    def __init__(self):

        """ Constructor of a number guessing game with 1 100 range number selection"""
        self.welcoming_message = "Welcome to the Number Guessing Game !"
        self.inferior_born = 0
        self.superior_born = 100 
        self.difficulty_selector_message = "Please select the difficulty level : "
        self.easy_difficulty_message = "1. Easy ( 10 chances)"
        self.medium_difficulty_message = "2. Medium ( 5 chances)"
        self.hard_difficulty_message = "3. Hard ( 3 chances)"
        self.chances = 0
        self.number = 0
        self.attempts = 0
        self.time_elapsed = 0
        self.highscore = 0
        self.difficulty_multiplier = 0

    def generate_number(self):
        """ Generate and returns  the number to guess in the mini-game in the int format
        """
        print("I'm thinking of a number between " + str(self.inferior_born) + " and " + str(self.superior_born) + ".")
        self.number = random.randint(self.inferior_born,self.superior_born)
        return self.number
    
    def set_easy_difficulty(self):
        """ Set the chances of guessing the number to 10 EASY 
        """
        print("Great ! You have selected the Easy difficulty level.")
        self.chances = 10
        self.difficulty_multiplier = 1
    
    def set_medium_difficulty(self):
        """ Set the chances of guessing the number to 5 MEDIUM
        """
        print("Great ! You have selected the Medium difficulty level.")
        self.difficulty_multiplier = 1.5
        self.chances = 5
    def set_hard_difficulty(self):
        """ Set the chances of guessing the number to 3 HARD 
        """
        print("Great ! You have selected the Hard difficulty level.")
        self.difficulty_multiplier = 3
        self.chances = 3
    def set_difficulty(self):
        """ Sets the desired difficulty of the game
        """
        print(self.difficulty_selector_message)
        print(self.easy_difficulty_message)
        print(self.medium_difficulty_message)
        print(self.hard_difficulty_message)
        user_input = input("Enter your choice: ")
        choice = int(user_input)
        try:
            match choice:
                case 1:
                    self.set_easy_difficulty()
                case 2:
                    self.set_medium_difficulty()
                case 3:
                    self.set_hard_difficulty()
                case _:
                    print("Not a valid number")
                    self.set_difficulty()
        except ValueError:
            print("Please enter a real number !")
            self.set_difficulty()

    def re_play_game(self):
        """Allow the user to play multiple rounds. Keep it playing until user decide to quit. 
        """
        user_input = input(" Do you want to play again Y/N ?")
        try:
            match user_input:
                    case 'Y' | 'y':
                        self.initialize_game()
                    case 'N' | 'n':
                        print("Total HighScore is "+ str(self.highscore)+".")
                        return 1
        except ValueError:
            print("Please anwser with Y/y or N/n.")
            
    def guess_the_number(self):
        """ Handles the logic to compare if we are less or greater than the guessed number.
        """
        is_winner = False
        base_winscore_earning = 100
        self.time_elapsed = time.time()
        while self.chances > 0:
            try:
                _input = input("Enter your guess: " )
                guess = int(_input)
            except ValueError:
                print("Error: Enter a valid number ! ")
                continue

            self.attempts += 1
            if guess == self.number:
                total_time = round(time.time() - self.time_elapsed)
                self.highscore += base_winscore_earning * self.difficulty_multiplier
                is_winner = True
                print("Congratulations! You guessed the correct number in "+ str(self.attempts) + " attempts.")
                print("Score is "+ str(self.highscore)+ ".")
                print(" Took the user "+ str(total_time) + " seconds to guess it correctly !")
                break
            
            self.chances -= 1
            if guess > self.number:
                print("Incorrect ! The number is less than " + _input + ".")
                base_winscore_earning -= 10
            else:
                print("Incorrect ! The number is greater than " + _input + ".")
                base_winscore_earning -= 10
        if not is_winner:      
            print("You ran out of chances ! The number was "+ str(self.number) + ".")
            self.time_elapsed = 0


    def initialize_game(self):
        """  Game logic is defined here 
        - First we generate the number betwwen Lower bound and Upper Bound .
        - Then we set the difficulty of the game e.g(easy,medium,hard)
        - Furthermore we run the prompt handler and main loop of the game.
        - Finally we ask the user if they want to replay the game with strings Y,y,N,n. 
        """

        print("Welcome to the Number Guessing Game !")
        self.time_elapsed = 0
        self.difficulty_multiplier = 0
        self.generate_number()
        self.set_difficulty()
        self.guess_the_number()
        self.re_play_game()

def main():
    game = NUMBER_GUESSING_GAME()
    game.initialize_game()
    


main()



        