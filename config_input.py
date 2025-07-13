from bot import Bot
from tower import Tower

def get_game_data():
    tower_range = validate_input_integer("Enter tower range: ")
    tower = Tower(tower_range)

    bot_count = validate_input_integer("Enter number of bots: ")
    
    bots = [fill_bot_data(i) for i in range(1, bot_count + 1)]

    return tower, bots


def validate_input_integer(promt):
    while True:
        try:
            value = int(input(promt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Emter a positive integer")


def fill_bot_data(index) -> Bot:
    print(f"\nBot {index} data:")

    name = input(f"Bot name: ").strip() or f"Bot{index}"
    distance = validate_input_integer("Bot distance: ")
    step = validate_input_integer("Enter bot step per round: ")

    return Bot(name=name, distance=distance, step=step)

