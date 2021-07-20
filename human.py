from player import Player
import re
#written by steve clark
class Human(Player):
    
    
    
    def __init__(self, name):
        super().__init__()
        
    def select_player_options(self, gameMode):
        player1Name = self.selectPlayerName(1)
        if gameMode == "Single player game":
            player2Name = "Computer"
        else:
            player2Name = self.selectPlayerName(2)
        playerNames= [player1Name, player2Name]
        return playerNames
    
    def selectPlayerNames(self, playerNumber):
        nameInput = input("Player " + " str(playerNumber) + ", "Enter your name!")
        playerName = self.validatePlayerName(nameInput)
        return playerName
    
    def validatePlayerName(self, rawNameInput): 
        if len(rawNameInput) < 2: 
            print("Player name must be 2 characters or more") 
            rawNameInput = input("Please enter your name: ")
            return self.validatePlayerName(rawNameInput) 
        elif len(rawNameInput) > 20: 
            print("Player name must be 20 characters or less") 
            rawNameInput = input("Please enter your name: ") 
            return self.validatePlayerName(rawNameInput)
        elif re.match("^[a-zA-Z0-9\s]*$", rawNameInput): 
            return rawNameInput 
        else: 
            print("Player name must contain only letters, numbers, or spaces") 
            rawNameInput = input("Please enter your name: ")
            return self.validatePlayerName(rawNameInput) 
