class Animal:
    def __init__(self, alive, fed, name):
        self.alive = True
        self.fed = False
        self.name = 'Волк из ну погоди'

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print('Съел')
            self.fed = True
        else:
            print('Не стал есть')
            self.alive = False


class Predator(Animal):
    def eat(self, food, name):
        if isinstance(food, Plant) and food.edible:
            print('Съел')
            self.fed = True
        else:
            print('Не стал есть')
            self.alive = False
            self.name = name

class Plant:
    def __init__(self, edible, name):
        self.edible = False
        self.name = 'Цветик семицветик'

class Flower(Plant):
    def __init__(self):
        self.type = type

class Fruit(Plant):
    def __init__(self, name):
        self.type = type
a1 = Predator('Волк из ну погоди')
a2 = Mammal('Рекс')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводное яблоко')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)