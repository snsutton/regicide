import hand

class player:

    MAX_HAND_SIZE = 8

    def __init__(self, name):
        self.name = name
        self.hand = hand.hand()
