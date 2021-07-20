from ai import AI
from human import Human
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

    def select_player_options(self, gameMode):
        player1Name = self.selectPlayerName(1)
        if gameMode == "Single player game":
            player2Name = AI
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

    
    def score_updater(self, result, player1, player2, hand1, hand2, score1, score2):
        handTitleList = ["Scissors", "Paper", "Rock", "Lizard", "Spock"] 
        handMessageList = ["Scissors (1) cuts Paper (2)", "Paper (2) covers Rock (3)", "Rock (3) crushes Lizard (4)", "Lizard (4) poisons Spock (5)", "Spock (5) smashes Scissors (1)", "Scissors (1) decapitates Lizard (4)", "Lizard (4) eats Paper (2)", "Paper (2) disproves Spock (5)", "Spock (5) vaporizes Rock (3)", "Rock (3) crushes Scissors (1)"]
        handTitle1 = handTitleList[hand1 - 1] 
        handTitle2 = handTitleList[hand2 - 1] 
        print(player1 + " selected " + handTitle1 + "(" + str(hand1) + ")") 
        print(player2 + " selected " + handTitle2 + "(" + str(hand2) + ")") 
        if (hand1 == 1 and hand2 == 2) or (hand1 == 2 and hand2 == 1): 
            print(" " + handMessageList[0]) 
        elif (hand1 == 2 and hand2 == 3) or (hand1 == 3 and hand2 == 2): 
            print(" " + handMessageList[1]) 
        elif (hand1 == 3 and hand2 == 4) or (hand1 == 4 and hand2 == 3): 
            print(" " + handMessageList[2]) 
        elif (hand1 == 4 and hand2 == 5) or (hand1 == 5 and hand2 == 4): 
            print(" " + handMessageList[3]) 
        elif (hand1 == 5 and hand2 == 1) or (hand1 == 1 and hand2 == 5): 
            print(" " + handMessageList[4]) 
        elif (hand1 == 1 and hand2 == 4) or (hand1 == 4 and hand2 == 1): 
            print(" " + handMessageList[5]) 
        elif (hand1 == 4 and hand2 == 2) or (hand1 == 2 and hand2 == 4): 
            print(" " + handMessageList[6]) 
        elif (hand1 == 2 and hand2 == 5) or (hand1 == 5 and hand2 == 2): 
            print(" " + handMessageList[7]) 
        elif (hand1 == 5 and hand2 == 3) or (hand1 == 3 and hand2 == 5): 
            print(" " + handMessageList[8]) 
        elif (hand1 == 3 and hand2 == 1) or (hand1 == 1 and hand2 == 3): 
            print(" " + handMessageList[9]) 
        else: 
            print("Players picked the same hand") 
        if result == "Player 1": 
            print(" " + player1 + " is the winner!") 
            score1 += 1 
        elif result == "Player 2": 
            print(" " + player2 + " is the winner!") 
            score2 += 1 
        else: 
            print("The game is tied!") 
        updatedScore = [score1, score2] 
        return updatedScore 

    def display_final_score(self, currentPlayers, finalScore): 
        print("Game over!" + currentPlayers[0], str(finalScore[0]) + ":" + str(finalScore[1]), currentPlayers[1] + " ")
    
    def calculate_round_result(self, player1HandPick, player2HandPick):
            if (player2HandPick - player1HandPick) % 5 in (1, 3): 
                roundResult = "Player 1" 
            elif (player2HandPick - player1HandPick) % 5 in (2, 4): 
                roundResult = "Player 2" 
            else: 
                roundResult = "Tie" 
            return roundResult
        
    def game_title_and_rules(self):
        self.gameTitle = "Game of Rock, Paper, Scissors, Lizard, Spock"
        self.gameRules = "Keyboard keys and game rules: 1: Scissors cuts Paper (2) and decapitates Lizard (4) 2: Paper covers Rock (3) and disproves Spock (5) 3: Rock crushes Scissors (1) and crushes Lizard (4) 4: Lizard eats Paper (2) and envenomates Spock (5) 5: Spock vaporizes Rock (3) and smashes Scissors (1)" 

    def display_title_rules(self):
        print(self.gameTitle)
        print(self.gameRules)
    
    def start_playing_game(self):
        titleAndRules = self.display_title_rules()
        modeInput = Game()
        gameMode = modeInput.select_game_mode()
        print()
        print(gameMode)
        playerInput = Human()
        playerNames = playerInput.select_player_options(gameMode)
        print(playerNames)
        gameScore = [0, 0]
        print()
        print(gameMode)
        print("playerName[0], str(gameScore[0], + " " + str(gameScore[1]),playerNames[1]")
        newRoundScore = self.play_next_round(gameMode, playerNames, gameScore)
        gameScore = gameScore.displayFinalScore(playerNames, newRoundScore)
    
    
        

            