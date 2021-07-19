class Player:
    def __init__(self, name, choice):
        self.name = name
        self.choice = self.player_choice()
        self.score = 0

    def player_choice(self):
        self.player_choice = input
