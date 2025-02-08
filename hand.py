class hand:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def __str__(self):
        card_ascii_lists = [card.__str__().split("\n") for card in self.hand]
        return "\n".join([" ".join(card_line) for card_line in zip(*card_ascii_lists)])

    def __repr__(self):
        return f"Hand of {len(self.hand)} cards"
