#inheritance
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def displayInfo(self):
#         print(f"브랜드: {self.brand} 모델: {self.model}")
#
# class Car(Vehicle):
#     def __init__(self, brand, model, engine):
#         super().__init__(brand,model)
#         self.engine = engine
#     def info(self):
#         self.displayInfo()
#         print(f"engine: {self.engine}")
#
#
# a = Car("벤츠","e클래스","V8")
# a.info()

class Monster:
    def __init__(self, HP, ATK):
        self.HP = HP
        self.ATK = ATK
    def hit(self):
        print(f"{self.ATK} 데미지 입힙니다.")

class Slime(Monster):
    def __init__(self,HP,ATK):
        super().__init__(HP,ATK)
    def defense(self):
        print(f"체력을 안 깎입니다.")

class Pig(Monster):
    def __init__(self,HP,ATK):
        super().__init__(HP,ATK)
    def rush(self):
        print(f"{self.ATK*2}의 데미지 입힙니다.(공격력 2배)")

class Wraith(Monster):
    def __init__(self,HP,ATK):
        super().__init__(HP,ATK)
        self.angry = 0
    def getAngry(self):
        self.angry += 10
    def getRage(self):
        print(f"분노! {self.ATK*5}의 데미지 입힙니다.(공격력 5배)")

a = Slime(10, 2)
a.defense()
b = Pig(50, 10)
b.hit()
b.rush()
c = Wraith(100, 20)
c.hit()
c.getAngry()
c.getRage()





































































