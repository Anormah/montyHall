import random

class MontyHall:
    def __init__(self):
        self.doors = [0, 0, 0]  # Initialisation des portes
        self.car_position = random.randint(0, 2)  # Position aléatoire de la voiture
        self.doors[self.car_position] = 1  # Place la voiture derrière l'une des portes
        self.user_choice = None
        self.reveal = None
        self.switch = False

    def reset(self):
        self.doors = [0, 0, 0]
        self.car_position = random.randint(0, 2)
        self.doors[self.car_position] = 1
        self.user_choice = None
        self.reveal = None
        self.switch = False

    def reveal_door(self):
        possible_reveals = [i for i in range(3) if i != self.user_choice and self.doors[i] == 0]
        self.reveal = random.choice(possible_reveals)

    def make_switch(self):
        self.switch = True
        self.user_choice = [i for i in range(3) if i != self.user_choice and i != self.reveal][0]

    def check_win(self):
        return self.doors[self.user_choice] == 1
