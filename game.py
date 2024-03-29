from collections import OrderedDict
from player import Player
import world
import time

def play():
    print("                                                                        ")
    print("                         Welcome to The Frozen Road")
    print("                                                                        ")   
    time.sleep(0.5)
    print("                                     |                                  ")
    time.sleep(0.5)
    print("                                 _  _|_  _                              ")
    time.sleep(0.5)
    print("                                |;|_|;|_|;|                             ")
    time.sleep(0.5)
    print("                                 \\.    .  /                             ")
    time.sleep(0.5)
    print("                                  \\:  .  /                              ")
    time.sleep(0.5)
    print("                                  ||:   |                               ")
    time.sleep(0.5)
    print("                                  ||:.  |                               ")
    time.sleep(0.5)
    print("                                  ||:  .|                               ")
    time.sleep(0.5)
    print("                                  ||:   |       \,/                     ")
    time.sleep(0.5)
    print("                                  ||: , |            /`\                ")
    time.sleep(0.5)
    print("                                  ||:   |                               ")
    time.sleep(0.5)
    print("                                  ||: . |                               ")
    time.sleep(0.5)
    print("     __                          _||_   |                               ")
    time.sleep(0.5)
    print("  `~    '--~~__            __ ----~    ~`---,              ___          ")
    time.sleep(0.5)
    print("               ~---__ ,--~'                  ~~----_____-~'   `~----~~\n")
    time.sleep(3)
    print("You're a traveler, Heading down this fozen road you find a cave. Might be what you need to survive the night.")
    time.sleep(1)
    print("Walking into the cave you find a small trapdoor on the ground that has been proped open by a stick. Your curiosity takes the better of you and you decend into the pit.")
    time.sleep(1)
    print("As you're climbing down this wooden latter you hear a snap and you fall to the floor.")
    time.sleep(2)

    
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            
            print("\n\nThe frozen road has consumed another traveler")
            time.sleep(0.5)
            print("                __)(__                       ")
            time.sleep(.05)
            print("          _____/      \\_____                ")
            time.sleep(0.5)
            print("         |  _     ___   _   ||               ")
            time.sleep(0.5)
            print("         | |  \    |   |  \ ||               ")
            time.sleep(0.5)
            print("         | |  |    |   |  | ||               ")
            time.sleep(0.5)
            print("         | |_/     |   |_/  ||               ")
            time.sleep(0.5)
            print("         | | \     |   |    ||               ")
            time.sleep(0.5)
            print("         | |  \    |   |    ||               ")
            time.sleep(0.5)
            print("         | |   \. _|_. | .  ||               ")
            time.sleep(0.5)
            print("         |                  ||               ")


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("What would you like to do?: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("No...You can't do that")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
