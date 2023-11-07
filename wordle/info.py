from math import log2
import os

class Information:
    def __init__(self):

        with open(os.path.join(os.path.dirname(__file__), "resources", "answers.txt")) as f:
            self.answers = f.read().split()
            # print(len(self.answers))

        with open(os.path.join(os.path.dirname(__file__), "resources", "allowed-guesses.txt")) as f:
            self.guesses = f.read().split()
            # print(self.guesses)

    def entropy(self, p, n):
        if p == 0 or n == 0:
            return 0
        
        return 0
    
    def format_feedback(self, dict):
        formatted_dict = ""
        for key, value in dict.items():
            formatted_dict += f"{key} [{' '.join(value)}]\n"
        return formatted_dict

    def feedback(self, guess, answer):
        
        if len(guess) != 5 or len(answer) != 5 or guess not in self.guesses or answer not in self.answers:
            return KeyError("Invalid Guess or Answer")

        info_ = []

        for i in range(len(guess)):
            if guess[i] == answer[i]:
                info_.append("G")
            elif guess[i] != answer[i] and guess[i] in answer:
                info_.append("Y")
            else:
                info_.append("X")

        return info_


    def remaining_possib(self, feedback, dictionary):
        # feedback = {word: feedback}
        # dictionary = [list of possible remaining words]
        possible_answers = list(dictionary)

        for guess, info in feedback.items():

            for feedback in info:

                if feedback == "G":
                    print(f"This is green, now we are inspecting the letter")
                    for word in possible_answers:
                        if word[i] != guess[i]:
                            possible_answers.remove(word)

                elif info[i] == "Y":
                    for word in possible_answers:
                        if word[i] == guess[i] or guess[i] not in word:
                            possible_answers.remove(word)

                elif info[i] == "X":
                    for word in possible_answers:
                        if guess[i] in word:
                            possible_answers.remove(word)


        return len(possible_answers), possible_answers



    

    


