import random

class Human:
    health = 100

    def __init__(self, health = 100):
        self.health = health

    def change_state(self, health = 0):
        self.health += health

        if self.health < 0:
            raise ValueError


# MAIN

h1 = Human(5)
h2 = Human(3)
h3 = Human(8)

while True:
    if h1 is not None:
        try:
            h1.change_state(health=random.randint(1, 3))
        except ValueError:
            print('У одного из персонажей закончилось здоровье!')
            h1 = None

    h2.change_state(health=random.randint(1, 3))
    h3.change_state(health=random.randint(1, 3))

    if h1 is None and h2 is None and h3 is None:
        break
