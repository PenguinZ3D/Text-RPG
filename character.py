from weapon import fists

class character:
    def __init__(self, name:str, health:int,):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

    

class Hero(character):
    def __init__(self, name: str, health: int):
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon

    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self):
        print(f"{self.name} dropped {self.weapon}")
        self.weapon = self.default_wepaon


class Enemy(character):
    def __init__(self, name: str, health: int, weapon):
        super().__init__(name=name, health=health)
        self.weapon = weapon