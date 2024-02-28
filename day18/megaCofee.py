import pandas
import faker
import random

f = faker.Faker('ko_KR')

aL = ['10', "20", "30", "40", "50", "60"]
aW = [20, 30, 30, 10, 5, 5]

cL = ['아이스아메리카노', '따뜻한아메리카노', '아이스라떼', '따뜻한라떼', '딸기라떼', '바닐라라떼', '민트모카']
cW = [30, 10, 10, 10, 20, 10, 10]

pL = ['현금', '체크카드', '신용카드', '카카오페이', '티머니']
pW = [5, 40, 40, 10, 5]

tL = ['아침','점심','저녁','밤']
tW = [60,30,10,10]

mega = {
    'c': [f.name() for i in range(1000)],
    'a': [random.choices(aL, weights=aW, k=1)[0] for i in range(1000)],
    'cf': [random.choices(cL, weights=cW, k=1)[0] for i in range(1000)],
    'p': [random.choices(pL, pW, k=1)[0] for i in range(1000)],
    't': [random.choices(tL, tW, k=1)[0] for i in range(1000)]
}
a = pandas.DataFrame(mega)
a.to_csv("mega.csv",index=False,encoding='utf-8-sig')