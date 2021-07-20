import re
# written by Steve Clark

class Game:
    
    
    def __init__(self):
        
        def select_game_mode(self):
            print ("To play against the computer, press 1. To play against another player, press 2")
        modeInput = input("Please select type of game you want to play! ")
        modeInput = self.validate_game_mode(modeInput)
        if modeInput == "1":
            game_mode = "Single Player Game"
        else:
            game_mode = "Multi Player Game"
        return game_mode
    
    
    def validate_game_mode(self, rawModeInput):
        if re.match("^[12]$", rawModeInput):
            return rawModeInput
        else:
            rawModeInput = input("Please press 1 or 2! ")
            return self.validate_game_mode(rawModeInput)
        
        
    def play_next_round(self):
        print("Would you like to play again?")
        nextRoundChoice = input("Please press y or n.")
        nextRoundChoice = self.validate_next_round_input(nextRoundChoice)
        return nextRoundChoice
    
    def validate_next_round_input(self, nextRoundInput):
        if re.match("^[yn]$", nextRoundInput):
            return nextRoundInput
        else:
            nextRoundInput = input("Press y or n to continue or stop!")
            return self.validate_next_round_input(nextRoundInput)
