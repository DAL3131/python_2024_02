# dataframe
import faker
import pandas

# data = {
#     '이름': ['기민서', '권성혁', '김태양', '안지우'],
#     '나이': [25, 15, 15, 21],
#     '거주지': ['과천시', '서울시', '서울시', '도쿄']
# }
# a = pandas.DataFrame(data)
# print(a)

import random


#
# fake = faker.Faker('ko_KR')
# name = [fake.name() for i in range(1000)]
# age = [random.randint(20, 50) for i in range(1000)]
# coffeeList = ['아아', '라떼', '모카', '바닐라', '디카페인']
# sellCoffee = [random.choice(coffeeList) for i in range(1000)]
#
# data = {
#     '이름': name,
#     '나이': age,
#     '구매한 커피': sellCoffee
# }
#
# b = pandas.DataFrame(data)
# print(b)
# b.to_csv('손놈List.csv')

# 일본 여행 관광객 리스트

# name: 한일미 [1000명]
# age: (10~70)
# tour: [맛집탐방,온천여행,야구관광,맥주투어,힐링]
def makeName():
    nationList = ['ko_KR', 'ja_JP', 'en_US']
    fake = faker.Faker(random.choice(nationList))
    return fake.name()


travelName = [makeName() for i in range(1000)]
travelAge = [random.randint(10, 71) for i in range(1000)]
travelTour = [random.choice(['맛집탐방', '온천여행', '야구관광', '맥주투어', '힐링']) for i in range(1000)]
travelCity = [random.choice(['후쿠오카', '벳푸', '오이타', '나가사키', '가고시마']) for i in range(1000)]
travelPlane = [random.choices(["제주항공", "에어서울", "티웨이", "진에어", "대한항공", "아시아나"], weights=[20, 20, 20, 20, 10, 10], k=1) for
               i in range(1000)]
japanTravel = {
    '이름': travelName,
    '나이': travelAge,
    '목적': travelTour,
    '도시': travelCity,
    '행기': travelPlane
}

c = pandas.DataFrame(japanTravel)
print(c)
c.to_csv('삼일절에 일본가는 한국인.csv')
