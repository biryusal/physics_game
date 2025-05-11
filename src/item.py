import numpy as np

class Item:
    def __init__(self, name: str, mass: float, **kwargs):
        self.name = name
        self.mass = mass
        self.cords = np.array([kwargs.get('x') or 0, kwargs.get('y') or 0, kwargs.get('z') or 0])

    def __str__(self):
        return self.name

    def change_position(self, cords: list[float, float, float]):
        self.cords = np.array(cords)