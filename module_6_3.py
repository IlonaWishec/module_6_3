import  random
class Animal:

        live = True
        sound = None
        _DEGREE_OF_DANGER = 0

        def __init__(self, speed):
                self._cords = [0, 0, 0]
                self.speed = speed

        def move(self, dx, dy, dz):
                new_z = self._cords[2] + dz * self.speed
                if new_z < 0:
                        print("It's too deep, I can't dive :(" )
                else:
                        self._cords[0] += dx * self.speed
                        self._cords[1] += dy * self.speed
                        self._cords[2] = new_z

        def get_cords(self):
                print(f'X: {self._cords[0]}', f'Y: {self._cords[1]}', f'Z: {self._cords[2]}')

        def attack(self):
                if Animal._DEGREE_OF_DANGER < 5:
                        print("Sorry, I'm peaceful")
                else:
                        print("Be careful, I'm attacking you 0_0")

class Bird(Animal):
        beak = True

        def lay_eggs(self):
                print(f'Here are (is) {random.randint(1,4)} eggs for you')

class AquaticAnimal(Animal):
        Animal._DEGREE_OF_DANGER = 3

        def dive_in(self, dz):
                dz_abs = abs(dz)
                new_z = self._cords[2] - (dz_abs/2) * self.speed
                if new_z < 0:
                        print("It's too deep, I can't dive :(")
                else:
                        self._cords[2] = int(new_z)

class PoisonousAnimal(Animal):
        Animal._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
        def speak(self):
                Animal.sound = 'Click - click - click'
                print(Animal.sound)



db = Duckbill(10)
print(db.live) #  True
print(db.beak) #  True
db.speak() #  Click - click - click
db.attack() #  Be careful, I'm attacking you 0_0
db.move(1, 2, 3)
db.get_cords() #  X: 10 Y: 20 Z: 30
db.dive_in(6)
db.get_cords() #  X: 10 Y: 20 Z: 0
db.lay_eggs() # Here are (is) 2 eggs for you



