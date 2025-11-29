from card import Card

class Enemy(Card):

    def __init__(self, enemy_card):
        super().__init__(enemy_card.rank, enemy_card.suit)
        self.enemy = enemy_card
        self.starting_health = 0

        if self.enemy.rank == "J":
            self.starting_health = 20
        elif self.enemy.rank == "Q":
            self.starting_health = 30
        elif self.enemy.rank == "K":
            self.starting_health = 40
        else:
            raise ValueError("Invalid enemy card rank")
        
        self.health_remaining = self.starting_health

    def __str__(self):
        return f"Enemy: \n{self.enemy} has {self.health_remaining} health remaining."
