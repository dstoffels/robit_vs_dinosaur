from combatant import Combatant


class Dinosaur(Combatant):
    def __init__(self, name, attack_power) -> None:
        super().__init__(name)
        self.attack_power = attack_power

    def get_damage(self):
        return self.attack_power + super().get_damage()
