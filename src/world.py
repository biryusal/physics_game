import numpy as np
from src.utils import set_interval
from src.item import Item
from src.types import Vector3D
from typing import TypedDict


class TypedItem(TypedDict):
    instance: Item
    velocity: Vector3D

class World:
    def __init__(self, fps: int) -> None:
        self.items: list[TypedItem] = []
        self.fps = fps

        set_interval(self.update, 1 / self.fps)

    def add_item(self, item: Item) -> None:
        self.items.append({"instance": item, "velocity": np.array([0, 0, 0])})

    @staticmethod
    def get_gravity_force(mass: float, gravitational_constant: float = 9.8) -> float:
        return mass * gravitational_constant

    @staticmethod
    def get_air_resistance_force(mass: float, velocity: Vector3D, air_density: float = 1.2) -> Vector3D:
        return -0.5 * velocity * mass * air_density

    def get_normal_force(self, mass: float, z_cord: float) -> float:
        if z_cord == 0:
            return -self.get_gravity_force(mass)

        return 0

    def get_net_force(self, mass: float, z_cord: float) -> float:
        return self.get_gravity_force(mass) + self.get_normal_force(mass, z_cord)

    def update(self) -> None:
        for item in self.items:
            item_instance = item["instance"]

            # Apply some X constant force
            applied_force = np.array([10, 0, 0])

            # Calculate net vertical force
            net_force_z = self.get_net_force(mass=item_instance.mass, z_cord=item_instance.cords[2])

            # Calculate new approximate position
            approx_new_position = item_instance.cords + applied_force + np.array([0, 0, net_force_z])

            # Calculate approximate velocity
            approx_velocity = (approx_new_position - item_instance.cords) / self.fps

            # Calculate air resistance with approximate velocity
            air_resistance = self.get_air_resistance_force(mass=item_instance.mass, velocity=approx_velocity)

            # Calculate new position
            new_position = approx_new_position + air_resistance

            # Calculate new velocity
            new_velocity = (new_position - item_instance.cords) / self.fps

            item["velocity"] = new_velocity
            item_instance.change_position(new_position)

            print(f"New position for item {item_instance.name}:", item_instance.cords)