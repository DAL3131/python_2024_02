# def solution(my_str, n):
#     res = []
#     print([my_str[i:i+n] for i in range(0,len(my_str),n)])
#
# def solution2(s):
#     words = s.split(" ")
#     jadenCaseWords = []
#     for i in words:
#
#         if i:
#             jadenCaseWord = i[0].upper() + i[1:].lower()
#         else:
#             jadenCaseWords = i
#         jadenCaseWords.append(jadenCaseWord)
#     return " ".join(jadenCaseWords)
# print(solution2("3people unFollowed me"))
# solution("adsfsadf", 6)

import pandas
import faker
fake = faker.Faker('ko_KR')
korName = [fake.name() for i in range(100)]
seriesName = pandas.Series(korName)
print(seriesName)
































