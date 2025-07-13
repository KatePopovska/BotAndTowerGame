from tower import Tower
from bot import Bot

class GameController:
    def __init__(self, bots, tower):
        self.bots = bots
        self.tower = tower
        self.round = 0
    
    def run_game(self):
        while self.bots:
            self.round +=1
            bots_in_range = [b for b in self.bots if self.tower.can_shoot(b)]
            if bots_in_range:
                bot = bots_in_range[0]
                self.bots.remove(bot)
                print(f"Round {self.round}: Tower shot {bot.name}")
            else:
                print(f"Round {self.round}: Tower did nothing")
            
            for bot in self.bots:
                bot.move()
                print(f"Bot {bot.name} moved to {bot.distance}")
                if bot.distance <= 0:
                    print("Game Over - Bot reached the tower")
                    return "defeat", self.round

        print(f"Victory! All bots destroyed in {self.round} rounds.")
        return "victory", self.round