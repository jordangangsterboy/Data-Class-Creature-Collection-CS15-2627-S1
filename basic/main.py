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

