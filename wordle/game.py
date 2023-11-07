import requests
import random
from info import Information as info
from colorama import Fore

class Game:
    def __init__(self):
        self.s = requests.Session()
        self.answer = random.choice(info().answers)
        # print(F"THE ANSWER IS {self.answer}")

        self.moves = 0

    def start(self):

        attempts, max_attempts, remaining_guesses = 0, 6, info().guesses

        all_guesses = {}

        while attempts < max_attempts:
            if attempts != 0:
                print(info().format_dict_as_string(all_guesses))
                print(f"Possible Answers: {info().remaining_possib(all_guesses, remaining_guesses)}")

            print(all_guesses)

            guess = input(f"Attempt {attempts + 1}: ")

            if len(guess) != 5 or guess.lower() not in info().guesses:
                print("Invalid Guess. Please try again.")
                continue

            attempts += 1

            if guess == self.answer:
                print(f"Congratulations! You've guessed the word! The word was {self.answer}")
                break
        

            all_guesses[guess.upper()] = info().feedback(guess, self.answer)


            
        if attempts == 6:
            print(f"Sorry, you've run out of attempts. The word was: {self.answer}")

        
    
    


    