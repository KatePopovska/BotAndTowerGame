from game_controller import GameController
from analyser import find_configuration_for_victory, analyse_game_result
from config_input import get_game_data

if __name__ == "__main__":
    tower, bots = get_game_data()
    original_bot_data = [(bot.name, bot.distance, bot.step) for bot in bots]
    game = GameController(bots, tower)
    result, rounds = game.run_game()
    if result is "defeat":
        victory_range, rounds = find_configuration_for_victory(
            start_range=tower.range + 1,
            max_range=100,
            bot_data=original_bot_data
        )
        analyse_game_result(tower_range=victory_range, rounds=rounds)
    