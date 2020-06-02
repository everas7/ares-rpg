from features.character import Character
from features.colors import colors
from data.magic import (fire_ball, wind_vortex,
    water_bullets)


player = Character(600, 300, 45, 50, 60, [fire_ball, wind_vortex, water_bullets])
enemy = Character(1000, 300, 35, 40, 40, [fire_ball, wind_vortex, water_bullets])

running = True
index = 0

print(colors.FAIL + colors.BOLD + "AN ENEMY APPEARD!" + colors.ENDC)

while running:
    print("=========================")
    player.choose_action()

    choice_index = int(input("Choose an action:")) - 1 
    if  choice_index is 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(colors.OKGREEN + "You perfomed a normal attack!")
        print("Damage dealt: " + str(dmg) + colors.ENDC)
    elif choice_index is 1:
        player.choose_spell()
        spell_choice_index = int(input("Choose a spell:")) - 1
        spell = player.spells[spell_choice_index]
        spell_dmg = spell.generate_damage()
        cost = spell.get_cost()

        if cost > player.get_mana():
            print(colors.FAIL + "Not enough mana" + colors.ENDC)
            continue

        player.decrease_mana(cost)
        enemy.take_damage(spell_dmg)
        print(colors.OKGREEN + "You casted a " + spell.get_name())
        print("Damage dealt: " + str(spell_dmg) + colors.ENDC)

    if enemy.get_hp() is 0:
        print(colors.OKGREEN + colors.BOLD + "Battle is over. You won!" + colors.ENDC)
        break

    enemy_choice_index = 0

    if enemy_choice_index is 0:
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print(colors.FAIL + "Enemy perfomed a normal attack!")
        print("Damage dealt: " + str(dmg) + colors.ENDC)


    print("-------------------------")
    print("Player HP: " + colors.OKGREEN + str(player.get_hp()) +"/" + str(player.get_max_hp()) + colors.ENDC)
    print("Player Mana: " + colors.OKBLUE + str(player.get_mana())  +"/" + str(player.get_max_mana()) + colors.ENDC)
    print("Enemy HP: " + colors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + colors.ENDC)
    print("Enemy Mana: " + colors.OKBLUE + str(enemy.get_mana()) + "/" + str(enemy.get_max_mana()) + colors.ENDC)


    if player.get_hp() is 0:
        print(colors.FAIL + colors.BOLD + "Battle is over. You lost!" + colors.ENDC)
        break

          



