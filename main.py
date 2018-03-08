# -*- coding: utf-8 -*-
from classes.game import Person, bcolors
magic = [{"name" : "Fire", "cost" : 10, "dmg": 60},
         {"name" : "Thunder", "cost" : 10, "dmg": 60},
         {"name" : "Blizzare", "cost" : 10, "dmg": 60}]
player = Person(460,65,60,34,magic)
enemy = Person(1200,65,45,25,magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!!!" + bcolors.ENDC)
while running:
    print("===============================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attcked for: ", dmg, "points of damage. Enemy HP: ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:"))-1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = 
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attcks for: ", enemy_dmg, "Player HP: ", player.get_hp())    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You WIN!!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + " Your enemy has defeated you!!!" + bcolors.ENDC)
        running = False