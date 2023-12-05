from math import log2
from collections import Counter
import os

class Information:
    def __init__(self):

        with open(os.path.join(os.path.dirname(__file__), "resources", "answers.txt")) as f:
            self.answers = f.read().split()
            # print(len(self.answers))

        with open(os.path.join(os.path.dirname(__file__), "resources", "allowed-guesses.txt")) as f:
            self.guesses = f.read().split()

    def feedback(self, answer, guess):
        if len(answer) != len(guess):
            raise ValueError("Word and guess must be the same length")
        
        feedback_string = ""

        for i in range(len(guess)):
            if guess[i] not in answer:
                feedback_string += "X"
            elif guess[i] in answer and guess[i] != answer[i]:
                feedback_string += "Y"
            elif guess[i] == answer[i]:
                feedback_string += "G"

        return feedback_string
    def clean_guesses(self, game_guesses, remaining_answers):
        for guess, feedback in game_guesses.items():
            for i, letter in enumerate(guess):
                if feedback[i] == "X":
                    # Letter not in word, remove all words containing this letter
                    remaining_answers = [answer for answer in remaining_answers if letter not in answer]
                elif feedback[i] == "Y":
                    # Letter in word but wrong position, remove words not containing this letter
                    # or having it in this position
                    remaining_answers = [answer for answer in remaining_answers if letter in answer and answer[i] != letter]
                elif feedback[i] == "G":
                    # Letter in correct position, keep words with this letter in the same position
                    remaining_answers = [answer for answer in remaining_answers if answer[i] == letter]

        return remaining_answers
    
    def format_feedback(self, all_guesses):
        feedback = ""
        for guess, fb in all_guesses.items():
            feedback += f"{guess}\n{fb}\n\n"
        return feedback
                
    def calculate_remaining_entropies(self, all_guesses):
        remaining_entropies = {}
        unguessed_words = self.clean_guesses(all_guesses, [word for word in self.answers if word not in all_guesses.keys()])
        
        for guess in unguessed_words:
            feedback_patterns = [self.feedback(word, guess) for word in unguessed_words]
            patterns = Counter(feedback_patterns)

            entropy = 0
            for count in patterns.values():
                probability = count / len(feedback_patterns)
                entropy += probability * log2(probability)

            remaining_entropies[guess] = entropy

        return remaining_entropies
    
    def max_entropy(self, remaining_entropies):
        return max(remaining_entropies, key=remaining_entropies.get)

    


