# dict_compre {k-v}
# key name: 추상적, 포괄적 이름이 좋다.
# coffee = {
#     '아메리카노':2.5,
#     '라떼':3,
#     '바닐라':3.5,
#     '코코아':3,
#     '민트모카':4,
# }
coffee = ['아메리카노', '라떼', '바닐라', '코코아', '민트모카']
price = [2.5, 3, 3.5, 3, 4]
# starbucks = list(zip(coffee,price)) #zipper
# megacoffee = dict(zip(coffee,price))
# print(starbucks)
# print(megacoffee)

# starbucks = [{'name':i, 'price':j} for i,j in zip(coffee,price)]
# print(starbucks)

# travelList = ['후쿠오카', '오사카', '도쿄', '삿포로', '오키나와']
# planePrice = [30, 40, 45, 50, 40]
#
# travel = [{'name': t, 'price': p} for t, p in zip(travelList, planePrice)]
# print(travel)









menu = ["americano", "latte", "mint", "hotchoco"]

#[{'name':'americano', 'wordLen':9

print([{'name':n, 'wordLen':len(n)} for n in menu])


