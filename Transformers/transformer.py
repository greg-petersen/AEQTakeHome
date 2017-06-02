class Transformer:

    def __init__(self, name, allegiance, strength, intelligence, speed, endurance, rank, courage, firepower, skill):
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
        winner = None

        # if self.name == 'Optimus Prime' or self.name == 'Predaking':
        #     winner = self
        # elif opponent.name == 'Optimus Prime' or opponent.name == 'Predaking':
        #     winner = opponent
        if self.courage - opponent.courage >= 4 and self.strength - opponent.strength >= 3:
            winner = self
        elif self.strength - opponent.strength >= 3 or \
                self.intelligence - opponent.intelligence >= 3 or \
                self.speed - opponent.speed >= 3 or \
                self.endurance - opponent.endurance >= 3 or \
                self.rank - opponent.rank >= 3 or \
                self.courage - opponent.courage >= 3 or \
                self.firepower - opponent.firepower >= 3 or \
                self.skill - opponent.skill >= 3:
            winner = self
        elif self.strength - opponent.strength <= -3 or \
                self.intelligence - opponent.intelligence <= -3 or \
                self.speed - opponent.speed <= -3 or \
                self.endurance - opponent.endurance <= -3 or \
                self.rank - opponent.rank <= -3 or \
                self.courage - opponent.courage <= -3 or \
                self.firepower - opponent.firepower <= -3 or \
                self.skill - opponent.skill <= -3:
            winner = opponent
        elif self.rating > opponent.rating:
            winner = self
        elif self.rating < opponent.rating:
            winner = opponent
        else:
            winner = 'Tie'
        # If winner = None, this means a tie occurred.
        return winner
