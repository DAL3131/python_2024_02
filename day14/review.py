# class Restaurant:
#     def __init__(self, name):
#         self.name = name
#         self.menuList = []
#     def appendMenu(self):
#         menu = input("추가할 메뉴:")
#         self.menuList.append(menu)
#         print(f"{menu} 메뉴가 추가되었습니다.")
#
#     def showmenu(self):
#         print(self.menuList)
#
#     def delMenu(self):
#         de = input("제거할 메뉴 입력:")
#         self.menuList.remove(de)
#         print(f"{de} 메뉴가 제거되었습니다.")
#
#
# a = Restaurant("배민")
#
# a.appendMenu()
# a.appendMenu()
# a.appendMenu()
# a.appendMenu()
# a.appendMenu()
#
# a.showmenu()
#
# a.delMenu()
# a.delMenu()
# a.delMenu()
#
# a.showmenu()

# 커피 메뉴[{'menu' : 'americano' , 'price : 3500}]


class Cafe:
    def __init__(self, name):
        self.name = name
        self.coffeeMenu = []
        self.partTime = []
        self.sales = 0

    def appendMenu(self):
        menu = input("추가할 커피 입력:")
        price = int(input("가격 입력:"))
        self.coffeeMenu.append({'name': menu, 'price': price})
        print(f"{menu} 커피가 추가되었습니다.")

    def showMenu(self):
        print(f"메뉴 리스트: {self.coffeeMenu}")

    def employ(self):
        job = input("고용할 알바생 이름:")
        self.partTime.append(job)

    def showJob(self):
        print(f"고용한 알바생 목록: {self.partTime}")

    def sell(self):
        # self.showMenu()
        # coffeeName = input("구매할 커피 이름:")
        # print(f"{coffeeName} 구매가 완료되었습니다.")
        # self.sales + self.coffeeMenu

        num = int(input(f"{self.coffeeMenu}중 번호를 고르세요:"))
        self.sales += self.coffeeMenu[num]['price']

    def sells(self):
        print(f"총 판매액은 {self.sales}입니다.")


c = Cafe("클래스카페")
c.appendMenu()
c.appendMenu()

c.sell()
c.sell()
c.sells()
