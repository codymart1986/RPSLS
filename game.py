from ai import AI
from human import Human
import re
#collaboration of Steve Clark and Cody Mart
class Game:
    def __init__(self):
        self.player_one = Human(self)
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

    
