import random

from game import Game
from ai import AI
from human import Human
from player import Player




def main():
    
    game = Game()
    game.startPlayingGame()
    
    
    if __name__ == "__main__":
        main()
        
def __init__(self):
    self.gameTitle = "Game of Rock, Paper, Scissors, Lizard, Spock"
    self.gameRules = "Keyboard keys and game rules: 1: Scissors cuts Paper (2) and decapitates Lizard (4) 2: Paper covers Rock (3) and disproves Spock (5) 3: Rock crushes Scissors (1) and crushes Lizard (4) 4: Lizard eats Paper (2) and envenomates Spock (5) 5: Spock vaporizes Rock (3) and smashes Scissors (1)" 

