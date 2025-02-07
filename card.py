class card:

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def __lt__(self, other):
        """
        Compare cards based on rank first, then suit.
        This enables sorting with the standard sort() function.
        """
        # Get numeric values for comparison
        self_rank_val = self.RANKS.index(self.rank)
        other_rank_val = self.RANKS.index(other.rank)
        self_suit_val = self.SUITS.index(self.suit)
        other_suit_val = self.SUITS.index(other.suit)
        
        # Compare ranks first, then suits if ranks are equal
        if self_rank_val == other_rank_val:
            return self_suit_val < other_suit_val
        return self_rank_val < other_rank_val
