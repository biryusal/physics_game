from src.types import Vector3D
import numpy as np

class Item:
    def __init__(self, name: str, mass: float, cords: Vector3D):
        self.name = name
        self.mass = mass
        self.cords = cords

    def __str__(self):
        return self.name

    def change_position(self, cords: Vector3D):
        self.cords = np.array(cords)