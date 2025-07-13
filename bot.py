class Bot:
    def __init__(self, name, distance, step):
        self.name = name
        self.distance = distance
        self.step = step

    def move(self):
        self.distance -= self.step