from combatant import Combatant
from weapon import Weapon


class Robot(Combatant):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.active_weapon = Weapon("Nunchaku", 20)

    def get_damage(self):
        return self.active_weapon.attack_power + super().get_damage()
