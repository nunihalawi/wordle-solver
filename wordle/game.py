import random
from info import Information as info
import pyperclip

class Game:
    def __init__(self):
        self.answer = random.choice(info().answers)
        # print(F"THE ANSWER IS {self.answer}")

    def start(self):

        attempts, max_attempts = 0, 6

        all_guesses = {}
        while attempts < max_attempts:
            if attempts > 0: print(f"The best guesses are: {info().max_entropy(info().calculate_remaining_entropies(all_guesses))}")

            guess = input("Enter a guess: ").lower()

            if guess not in info().answers:
                print("Invalid guess")
                continue # restart the loop if the guess is invalid
            
            attempts += 1
            all_guesses[guess] = info().feedback(self.answer, guess)

            print(info().format_feedback(all_guesses))

            if guess == self.answer:
                print(f"You won! The word was {self.answer}")
                break # exit the loop if the guess is correct
            
            if attempts == max_attempts:
                print(f"You lost! The word was {self.answer}")
                break


        
    
    


    