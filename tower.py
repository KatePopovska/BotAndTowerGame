class Tower:
    def __init__(self, range):
        self.range = range
        self.skiped_roundes = 0

    def can_shoot(self, bot):
        is_shoot = self.range >= bot.distance
        if not is_shoot: self.skiped_roundes +=1
        return is_shoot
    