from character import Hero, Enemy
from weapon import short_bow, iron_sword

end_game = True

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

while end_game:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")

    input()
        

    if hero.health == 0 or enemy.health == 0:
        end_game = False