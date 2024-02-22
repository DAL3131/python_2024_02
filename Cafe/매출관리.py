# class Cafe:
#     def __init__(self, name):
#         self.name = name
#         self.menu = []
#         self.sales = 0
#
#     def addCoffee(self):
#         coffeeName = input("추가할 커피 이름:")
#         coffeePrice = int(input(f"{coffeeName} 가격:"))
#         coffeeDic = {'이름': coffeeName, '가격': coffeePrice}
#         self.menu.append(coffeeDic)
#         print(f"{coffeeName}가 추가되었습니다.")
#
#     def showMenu(self):
#         print(self.menu)
#
#     def sell(self):
#         sellCoffee = int(input(f'{self.menu} 중 구매할 커피 번호:'))
#         self.sales += self.menu[sellCoffee - 1]['가격']
#         print(f'현매출 {self.sales}')
#
#
# a = Cafe('커피파는곳')
# a.addCoffee()
# a.addCoffee()
# a.addCoffee()
# a.addCoffee()
#
# a.showMenu()
# a.sell()
# a.sell()
