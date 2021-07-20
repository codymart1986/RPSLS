from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__(self)

    def cpu_choice(self):
        self.cpu_choice = random.randint(1, 5)

        if self.cpu_choice == 1:
            print("CPU has chosen Rock")
        elif self.cpu_choice == 2:
            print("CPU has chosen Paper")
        elif self.cpu_choice == 3:
            print("CPU has chosen Scissors")
        elif self.cpu_choice == 4:
            print("CPU has chosen Lizard")
        elif self.cpu_choice == 5:
            print("CPU has chosen Spock")