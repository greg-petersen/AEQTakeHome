class Transformer:
    def __init__(self, name, allegiance, strength, intelligence, speed, endurance, rank, courage, firepower, skill):
        """Initialization function for a Transformer."""
        self.name = name
        self.allegiance = allegiance
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed
        self.endurance = endurance
        self.rank = rank
        self.courage = courage
        self.firepower = firepower
        self.skill = skill
        self.rating = strength + intelligence + speed + endurance + firepower
        self.alive = True

    def fight(self, opponent):
        """Determines, between two transformers, who is the winner based on the following conditions."""
        winner = None

        if (self.name == 'Optimus Prime' or self.name == 'Predaking') and \
            (opponent.name == 'Optimus Prime' or opponent.name == 'Predaking'):
            winner = 'Optoking'
        elif self.name == 'Optimus Prime' or self.name == 'Predaking':
            winner = self
        elif opponent.name == 'Optimus Prime' or opponent.name == 'Predaking':
            winner = opponent
        elif self.courage - opponent.courage >= 4 and self.strength - opponent.strength >= 3:
            winner = self
        elif opponent.courage - self.courage >= 4 and opponent.strength - self.strength >= 3:
            winner = opponent
        elif self.skill - opponent.skill >= 3:
            winner = self
        elif opponent.skill - self.skill >= 3:
            winner = opponent
        elif self.rating > opponent.rating:
            winner = self
        elif self.rating < opponent.rating:
            winner = opponent
        else:
            winner = 'Tie'
            self.alive = False
            opponent.alive = False

        if winner == self:
            opponent.alive = False
        elif winner == opponent:
            self.alive = False

        return winner
