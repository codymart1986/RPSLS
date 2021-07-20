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

        layers = int(input('How many people are playing? 1 or 2?:'))
        if players == 1:
            self.player_1 = Human()
            self.player_1.user_name()
            print(f"Player 1's name is: {self.player_1.name}")
            self.player_2 = Computer()
        else:
            self.player_1 = Human()
            self.player_1.user_name()
            print(f"Player 1's name is: {self.player_1.name}")
            print()
            self.player_2 = Human()
            self.player_2.user_name()
            print(f"Player 2's name is: {self.player_2.name}")
            print()

    def player1_choice(self):
        valid = False
        while valid == False:
            player1_gesture = int(input('Choose a gesture to use this round Rock = 0, Paper = 1, Scissors = 2, '
                                        'Lizard = 3, Spock = 4: '))
            if player1_gesture != 0 and player1_gesture != 1 and player1_gesture != 2 and player1_gesture !=3 and player1_gesture != 4:
                print("Please enter a valid input!")
            else:
                valid = True
            gesture_chosen = self.gestures[player1_gesture]
            return gesture_chosen

    def player2_choice(self):
        if self.player_2.name == 'AI':
            player_2_choice = random.randint(0, 4)
            gesture_chosen = self.gestures[player_2_choice]
            return gesture_chosen
        else:
            valid = False
            while valid == False:
                player2_gesture = int(input('Choose a gesture to use this round Rock = 0, Paper = 1, Scissors = 2, '
                                            'Lizard = 3, Spock = 4: '))
                if player2_gesture != 0 and player2_gesture != 1 and player2_gesture != 2 and player2_gesture != 3 \
                        and player2_gesture != 4:
                    print("Please enter a valid input!")
                else:
                    valid = True
                gesture_chosen = self.gestures[player2_gesture]
                return gesture_chosen

    def current_round(self):
        p1_gesture = self.player1_choice()
        p2_gesture = self.player2_choice()

        if p1_gesture == p2_gesture:
            print("TIE, TRY AGAIN!")
            self.rounds += 1
        elif p2_gesture in self.player_1.wins_against:
            print(f"{self.player_1.name} Wins this round!")
            self.rounds += 1
            self.player_1.score += 1
        else:
            print(f"{self.player_2.name} Wins this round!")
            self.rounds += 1
            self.player_2.score += 1

    def winner(self):
        if self.player_1.score == 3:
            print(f"{self.player_1.name} Beat {self.player_2.name}")
        elif self.player_2.score == 3:
            print(f"{self.player_2.name} Beat {self.player_1.name}")

    def rematch(self):
        validation = input("Would you like to rematch?")
        if validation == "y":
            self.player_1.score = 0
            self.player_2.score = 0
        else:
            self.run = False

    
