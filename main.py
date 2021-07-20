
from game import Game


def main():
    
    game = Game
    game.welcome_message()
    game.select_game_mode()
    game.selectPlayerNames()
    game.start_playing_game()
    
    
if __name__ == "__main__":
    main()
