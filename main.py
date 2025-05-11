import threading
import numpy as np

def set_interval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

class Item:
    def __init__(self, name: str, mass: float, **kwargs):
        self.name = name
        self.mass = mass
        self.cords = np.array([kwargs.get('x') or 0, kwargs.get('y') or 0, kwargs.get('z') or 0])

    def __str__(self):
        return self.name

    def change_position(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class World:
    def __init__(self, fps: int):
        self.items: list = []
        self.fps = fps

        set_interval(self.update, 1 / self.fps)

    def add_item(self, item: Item):
        self.items.append(item)

    @staticmethod
    def get_gravity_force(mass: float, gravitational_constant: float = 9.8):
        return mass * gravitational_constant

    def get_normal_force(self, mass: float, z_cord: int):
        if z_cord == 0:
            return -self.get_gravity_force(mass)

        return 0

    def get_net_force(self, mass: float):
        return self.get_gravity_force(mass) + self.get_normal_force(mass)

    def get_air_resistance_force(self, mass: float):
        return 0

    def update(self):
        for item in self.items:
            item.change_position(item.x, item.y, self.get_net_force(item.mass))


def main():
    current_world = World(fps=60)
    first_item = Item(mass=10, name="First item in this world!")

    # I am above the first item
    second_item = Item(mass=10, name="First item in this world!", z=200)

    current_world.add_item(first_item)
    current_world.add_item(second_item)

if __name__ == '__main__':
    main()