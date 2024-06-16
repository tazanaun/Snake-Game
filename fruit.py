import random

class Fruit:
        def __init__(self):
            random.seed()
            isEaten = False
            xpos = random.randint(0,512)
            ypos = random.randint(0,512)