# filter
# lambda x,y 합, 차, 곱

# lambda x,y:x+y
# lambda x,y:x-y
# lambda x,y:x*y
# a = lambda x:x.upper()

# map(how, what) : what을 how로 바꿔주기
# rank =  ['이병', '일', '상', '병장']
# def rankToSalary(rank):
#     salrary = {
#         '이병':60,
#         '일':68,
#         '상':80,
#         '병장':100,
#     }
#     return salrary[rank]
# res = map(rankToSalary, rank)
# salaryList = list(res)
# print(salaryList)

# filter(how, what):걸러주기
# res = filter(lambda x:x>5,list)
# filterList = list(res)
# print(filterList)
# evenList = [2,4,6,8,10]
# res2 = filter(lambda x:x%4 == 0, evenlist)
# filterL = evenlist(res2)
# print(filterL)

# fruits = ['mandarin','kiwi','orange','apple','peach','banana']
# fruitsFilter = filter(lambda x:len(x)>=6, fruits)
# print(list(fruitsFilter))
#
# fruitsFil = filter(lambda x:x[0]== 'a' or x[1]== 'a' , fruits)
# print(list(fruitsFil))
#
# numbers = [5,10,15,20,25]
# # numbers를 각각 제곱해주기
# fmap = map(lambda x:x**2, numbers)
# sfilt = filter(lambda x:50 <= x <= 500, fmap)
# print(list(sfilt))

words = ['hello','world','python','is','crazy']
res = filter(lambda x:len(x)>=5,words)
res1 = map(lambda x:x.upper(), res)
print(list(res1))



