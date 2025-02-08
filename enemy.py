class Enemy:

    def __init__(self, enemy_card):
        self.enemy = enemy_card
        self.health = 0

        if self.enemy.rank == "J":
            self.health = 20
        elif self.enemy.rank == "Q":
            self.health = 30
        elif self.enemy.rank == "K":
            self.health = 40
        else:
            raise ValueError("Invalid enemy card rank")
        
        self.health_remaining = self.health

    def __str__(self):
        return f"Enemy: \n{self.enemy} has {self.health_remaining} health remaining."