class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        if species == 'mammal':
            species_names = self.mammals
            names = ', '.join(species_names)
            result = f'Mammals in {zoo_name}: {names}\n'
        elif species == 'fish':
            species_names = self.fishes
            names = ', '.join(species_names)
            result = f'Fishes in {zoo_name}: {names}\n'
        elif species == 'bird':
            species_names = self.birds
            names = ', '.join(species_names)
            result = f'Birds in {zoo_name}: {names}\n'
        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
i = 0
while True:
    if i >= n:
        break
    i += 1
    animals = input().split()
    zoo.add_animal(animals[0], animals[1])
info = input()
print(zoo.get_info(info))
