class Hand:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def __str__(self):
        card_ascii_lists = [card.__str__().split("\n") for card in self.hand]
        return "\n".join([" ".join(card_line) for card_line in zip(*card_ascii_lists)])

    def __repr__(self):
        return f"Hand of {len(self.hand)} cards"
    
    def __iter__(self):
        return iter(self.hand)
    
    def __len__(self):
        return len(self.hand)
    
    def __getitem__(self, index):
        return self.hand[index]
    
    def sort(self):
        self.hand.sort()
        self.hand.reverse()

    def remove(self, card):
        self.hand.remove(card)
