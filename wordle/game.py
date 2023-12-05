import random
from info import Information as info
import pyperclip

class Game:
    def __init__(self):
        self.answer = random.choice(info().answers)
        self.possibilities = info().guesses


        # print(F"THE ANSWER IS {self.answer}")

    def start(self):

        attempts, max_attempts = 0, 6

        all_guesses = {}
        while attempts < max_attempts:
            if attempts > 0: 
                best_guess = info().max_entropy(info().calculate_remaining_entropies(all_guesses))
                print(f"The best guess is {best_guess}")

            guess = input("Enter a guess: ").lower()

            if guess not in info().answers:
                print("Invalid guess")
                continue # restart the loop if the guess is invalid
            
            attempts += 1
            # Format the guess
            all_guesses[guess] = info().feedback(self.answer, guess)
            #Clean the remaining possible guesses from the information we have just collected
            self.guesses = info().clean_guesses(all_guesses, self.possibilities)
            # Print the guess for the user
            print(info().format_feedback(all_guesses))

            if guess == self.answer:
                print(f"You won! The word was {self.answer}")
                break # exit the loop if the guess is correct
            
            if attempts == max_attempts:
                print(f"You lost! The word was {self.answer}")
                break


        
    
    


    