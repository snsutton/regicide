import hand


class Player:

    MAX_HAND_SIZE = 8

    def __init__(self, name):
        self.name = name
        self.hand = hand.Hand()

    def __str__(self):
        return f"{self.name}'s hand:\n{self.hand}"
