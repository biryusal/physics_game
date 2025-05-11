from src.world import World
from src.item import Item

def main():
    current_world = World(fps=60)
    first_item = Item(mass=10, name="First item spawned in this world!")

    # I am above the first item
    second_item = Item(mass=10, name="Second item spawned in this world!", cords=(0, 0, 200))

    current_world.add_item(first_item)
    current_world.add_item(second_item)

if __name__ == '__main__':
    main()