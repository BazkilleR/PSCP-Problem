"""Impostor"""
import json

def amongus():
    """Impostor"""
    alive = {}
    dead = {}

    while True:
        text = input()

        if text == "Start":
            break

        alive.update(json.loads(text))

    while True:
        dead_input = input()

        if dead_input == "End":
            break

        who_dead = alive.pop(dead_input)
        dead.update({dead_input : who_dead})

    imposter_count = 0
    for i in list(alive.values()):
        imposter_count += 1 if i == "Impostor" else 0

    sorted_alive = sorted(alive)
    sorted_dead = sorted(dead)

    print(f"{imposter_count} Impostor Remains")
    print("***Alive***")
    for color in sorted_alive:
        print(f"{color} : {alive[color]}")
    print("***Dead***")
    for color in sorted_dead:
        print(f"{color} : {dead[color]}")

amongus()
