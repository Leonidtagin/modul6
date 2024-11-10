class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name



class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print('Съел')
            self.fed = True
        else:
            print('Не стал есть')
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print('Съел')
            self.fed = True
        else:
            print('Не стал есть')
            self.alive = False

class Plant:
    def __init__(self, name):
        super().__init__()
        self.edible = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True
        pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с уолл стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)