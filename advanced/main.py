import dataclasses

@dataclasses.dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float

dragon = Creature("Jordan", "Dragon", 6, 100.0)
gorilla = Creature("John", "Gorilla", 6, 100.0)
zebra = Creature("Sean", "Zebra", 6, 100.0)
python = Creature("Tyrone", "Python", 6, 100.0)
print(dragon.name)
print(dragon.species)
print(dragon.level)
print(dragon.health)
print(gorilla.name)
print(gorilla.species)
print(gorilla.level)
print(gorilla.health)
print(python.name)
print(python.species)
print(python.level)
print(python.health)
print(zebra.name)
print(zebra.species)
print(zebra.level)
print(zebra.health)

dragon.level = 7
print(dragon.level)
dragon.health = 96.0
print(dragon.health)
print(gorilla.health)

print("Now you're going to make your own creature.")
new_name = input("Type in the creature's name: ")
new_species = input("Type in the creature's species: ")

while True:
    try:
        new_level = int(input("Type the creature's level: "))
        break
    except ValueError:
        print("Enter a valid integer for the level.")
while True:
    try:
        new_health = float(input("Type in the creature's health: "))
        break
    except ValueError:
        print("Type in a valid number for the health.")

user_creature = Creature(new_name, new_species, new_level, new_health)

print("Now you're going to make your own creature.")
print(user_creature.name)
print(user_creature.species)
print(user_creature.level)
print(user_creature.health)

