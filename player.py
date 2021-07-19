class Player:
    def __init__(self, name, choice):
        self.name = name
        self.choice = self.player_choice()
        self.score = 0

    def player_choice(self):
        self.player_choice = int(input("Select a gesture!"))
        
        if self.player_choice < 1 or self.player_choice > 5:
            print("Invalid input, try again!")
            self.player_choice
        elif self.player_choice == 1:
            print("You have chosen Rock")
        elif self.player_choice == 2:
            print("You have chosen Paper")
        elif self.player_choice == 3:
            print("You have chosen Scissors")
        elif self.player_choice == 4:
            print("You have chosen Lizard")
        elif self.player_choice == 5:
            print("You have chosen Spock")


