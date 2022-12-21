from robot import Robot
from dinosaur import Dinosaur
import random


class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("R2D2")
        self.dinosaur = Dinosaur("Littlefoot", 20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur")

    def battle_phase(self):
        while self.robot.is_alive() and self.dinosaur.is_alive():
            if random.randint(0, 1) == 0:
                self.robot.attack(self.dinosaur)
                self.dinosaur.attack(self.robot)
            else:
                self.dinosaur.attack(self.robot)
                self.robot.attack(self.dinosaur)

    def display_winner(self):
        winner = None
        if self.robot.is_alive():
            winner = self.robot
        else:
            winner = self.dinosaur
        print(f'{winner.name} is the victor!')
