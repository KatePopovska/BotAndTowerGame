from tower import Tower
from bot import Bot
from game_controller import GameController

def find_configuration_for_victory(start_range, max_range, bot_data):
    for tower_range in range(start_range, max_range):
        bots_copy = [Bot(name, distance, step) for (name, distance, step) in bot_data]
        tower = Tower(range=tower_range)
        game = GameController(bots_copy, tower)
        result, rounds  =game.run_game()
        if result == "victory":
            return tower_range, rounds
    return None, None

def analyse_game_result(tower_range, rounds):
    if tower_range is not None:
         print(f"Victory possible with tower range: {tower_range} (in {rounds} rounds)")
    else:
         print("Victory is NOT possible at any tower range.")

