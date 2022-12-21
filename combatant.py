import random


class Combatant:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 200

    def is_alive(self):
        return self.health > 0

    def get_damage(self):
        return random.randint(-15, 15)

    def attack(self, combatant):
        if self.is_alive():
            damage = self.get_damage()
            combatant.health -= damage

            print()
            print(
                f"{self.name} attacks {combatant.name} for {damage} damage!")
            print(f"{combatant.name} now has {combatant.health} health remaining.")
            print()
