class Player:
    def __init__(self, name):
        self.name = name
        self.choice = self.player_choice()
        self.score = 0

    def player_choice(self):
        isValid = False
        while isValid == False:
            self.human_choice = (input("Select a gesture! \n 1 = Rock \n 2 = Paper \n 3 = Scissors \n 4 = Lizard \n 5 = Spock \n"))
            if self.human_choice == 1:
                isValid = True
                print("You have chosen Rock")
            elif self.human_choice == 2:
                isValid = True
                print("You have chosen Paper")
            elif self.human_choice == 3:
                isValid = True
                print("You have chosen Scissors")
            elif self.human_choice == 4:
                isValid = True
                print("You have chosen Lizard")
            elif self.human_choice == 5:
                isValid = True
                print("You have chosen Spock")
            else:
                print("Please return to the Derek Zoolander Center for Kids Who Can't Read Good")
                Player(self.name)
            return self.human_choice
