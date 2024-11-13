import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self.cords = [0, 0, 0]
        self.speed = speed
    def move(self, dx, dy, dz):
        if self._cords [2] + dz < 0:
            print("It's too deep, I can't dive):(")
        else:
           self._cords [0] += dx * self.speed
           self._cords [1] += dy * self.speed
           self._cords [2] += dz * self.speed

    def get_cords(self):
        return f"X: {self._cords}, [0] Y: {self._cords}, [1] Z: {self._cords}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, attacking you 0_0")

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        num_eggs = random.randit(1, 4)
        print(f"Here are(is) {num_eggs} eggs for you")

class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        z_change = abs(dz) * self.speed / 2
        new_z = self._cords[2] - z_change
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z


class PoisonousAnimal(Animal):
     def __init__(self, speed):
         super().__init__(speed)
         self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        self.sound = 'Click - Click - Click'

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()




