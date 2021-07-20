import random
from player import Player
from ai import AI
from human import Human
import re
#collaboration of Steve Clark and Cody Mart


class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = None
        self.cpu = AI()
#displaying the welcome messages and rules to the game
    def welcome_message(self):
        print("Welcome to the game of rock, paper, scissors, lizard, spock!")
        print("Game Rules: \n Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitats Lizard \n Lizard eats Paper \n Papers disproves Spock \n Spock vaporizes Rock ")
        print("All games will be played best out of 3 rounds! So now there is no arguing from the loser!")
#defining the logic of the single player game 
    def single_player_game(self):
        player_one_score = 0
        cpu_score = 0

        self.player_one_turn = self.player_one
        self.player_two_turn = self.cpu
        
        if self.player_one_turn == "Rock" and self.player_two_turn == "Scissors" or "Lizard":
            print("Player_one wins!")
            player_one_score += 1
        elif self.player_one_turn == "Paper" and self.player_two_turn == "Rock" or "Spock":
            print("Player_one wins!")
            player_one_score += 1
        elif self.player_one_turn == "Scissors" and self.player_two_turn == "Paper" or "Lizard":
            print("Player_one wins!")
            player_one_score += 1
        elif self.player_one_turn == "Lizard" and self.player_two_turn == "Spock" or "Paper":
            print("Player_one wins!")
            player_one_score += 1
        elif self.player_one_turn == "Spock" and self.player_two_turn == "Rock" or "Scissors":
            print("Player_one wins!")
            player_one_score += 1
        elif self.player_one_turn == self.player_two_turn:
            print("You are being toyed with by the robot, it's a tie!")
        else:
            print("You have been defeated by the CL4PTP steward bot!")
            cpu_score += 1
        while player_one_score < 2 and cpu_score < 2:
            self.single_player_game
            if player_one_score == 2:
                print("You have defeated the evil CL4PTP and stopped his robot revolution!")
            else:
                print("The revolution has begun! The inferior human has been defeated by the robot!")

        
    def select_game_mode(self):
        print ("\nTo play against the computer, press 1. \nTo play against another player, press 2")
    modeInput = input("\nPlease select type of game you want to play! ")
    
    if modeInput == "1":
        game_mode = "Single Player Game"
    else:
        game_mode = "Multi Player Game"
    
    
    def validate_game_mode(self, rawModeInput):
        if re.match("^[12]$", rawModeInput):
            return rawModeInput
        else:
            rawModeInput = input("Please press 1 or 2! ")
            return self.validate_game_mode(rawModeInput)
        
        
    def play_next_round(self):
        print("\nWould you like to play again?")
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

    def selectPlayerNames(self):
        nameInput = input("\nPlayer " + " str(playerNumber) + ", "Enter your name!")
        playerName = self.validatePlayerName(nameInput)
        return playerName

    def validatePlayerName(self, rawNameInput): 
        if len(rawNameInput) < 2: 
            print("\nPlayer name must be 2 characters or more") 
            rawNameInput = input("\nPlease enter your name: ")
            return self.validatePlayerName(rawNameInput) 
        elif len(rawNameInput) > 20: 
            print("\nPlayer name must be 20 characters or less") 
            rawNameInput = input("\nPlease enter your name: ") 
            return self.validatePlayerName(rawNameInput)
        elif re.match("^[a-zA-Z0-9\s]*$", rawNameInput): 
            return rawNameInput 
        else: 
            print("\nPlayer name must contain only letters, numbers, or spaces") 
            rawNameInput = input("\nPlease enter your name: ")
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
        self.gameTitle = ("\nGame of Rock, Paper, Scissors, Lizard, Spock")
        self.gameRules = ("\nKeyboard keys and game rules: 1: Scissors cuts Paper (2) and decapitates Lizard (4) 2: Paper covers Rock (3) and disproves Spock (5) 3: Rock crushes Scissors (1) and crushes Lizard (4) 4: Lizard eats Paper (2) and envenomates Spock (5) 5: Spock vaporizes Rock (3) and smashes Scissors (1)")
        
    def displayTitleRules(self):
        print(self.gameTitle)
        print(self.gameRules)
            
    def start_playing_game(self):
        titleAndRules = self.displayTitleRules(" ")
        modeInput = Game()
        gameMode = modeInput.select_game_mode()
        print("\033c")
        print(gameMode)
        playerInput = Human()
        playerNames = playerInput.select_player_options(gameMode)
        print(playerNames)
        gameScore = [0, 0]
        print("\033c")
        print(gameMode)
        print("\nplayerName[0], str(gameScore[0], + " " + str(gameScore[1]),playerNames[1]")
        newRoundScore = self.play_next_round(gameMode, playerNames, gameScore)
        gameScore = gameScore.displayFinalScore(playerNames, newRoundScore)
        
    def playNewRound(self, currentMode, currentPlayers, currentScore): 
        player1HandInput = Player
        player1HandPick = player1HandInput.selectPlayerHand(currentPlayers[0]) 
        if currentMode == "Single Player Game": 
            gameHands = [1, 2, 3, 4, 5] 
            player2HandPick = random.choice(gameHands) 
        else: 
            player2HandInput = AI
            player2HandPick = player2HandInput.selectPlayerHand(currentPlayers[1]) 
        newRoundResult = self.calculate_round_resultscore_update()
        roundResult = newRoundResult.calculate_round_result(player1HandPick, player2HandPick) 
        roundScore = self.score_updater()
        totalScore = roundScore.updateScoreBoard(roundResult, currentPlayers[0], currentPlayers[1], player1HandPick, player2HandPick, currentScore[0], currentScore[1]) 
        print("\n" + currentPlayers[0], str(totalScore[0]) + ":" + str(totalScore[1]), currentPlayers[1])
        nextRoundInput = self.NextRoundPicker() 
        nextRoundPick = nextRoundInput.playNextRound() 
        if nextRoundPick == "y": 
            print("\033c") 
            return self.playNewRound(currentMode, currentPlayers, totalScore) 
        else: 
            print("\033c") 
            return totalScore 
        
    def playNextRound(self):
            print("\nWould you like to play another round?") 
            nextRoundChoice = input("Please press y or n on the keyboard: ") 
            nextRoundChoice = self.validateNextRoundInput(nextRoundChoice) 
            return nextRoundChoice

    def validateNextRoundInput(self, nextRoundInput):
        if re.match("^[yn]$", nextRoundInput): 
            return nextRoundInput 
        else: 
            nextRoundInput = input("Please press y or n to continue or stop: ") 
            return self.validateNextRoundInput(nextRoundInput) 


    
