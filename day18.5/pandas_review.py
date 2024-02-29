import random

import pandas
import faker

fake = faker.Faker("ko_KR")

#cgv 일일 매출표
# name
# male
# movie
# snack

cgvData = {
    'name' : [fake.name() for i in range(100)],
    'male' : [random.choice(["남","여"]) for  i in range(100)],
    'movie' : [random.choice(["듄", "파묘","웡카","티라노","귀칼"])for  i in range(100)],
    'snack' : [random.choice(["팝콘", "오징어","콜라","맛밤","커피"])for  i in range(100)],
}

a = pandas.DataFrame(cgvData)
a.to_csv("cgv.csv", index=False, encoding="utf-8-sig")