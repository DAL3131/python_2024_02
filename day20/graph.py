import matplotlib.pyplot as plt
import pandas
# x = [1, 2, 3, 4, 5]
# y = [30, 40, 50, 60, 70]
# plt.plot(x, y)
# plt.show()

# 히스토그램

# data = [1,1,2,3,4,6,7,7,9,10]
# plt.hist(data)
# plt.show()

# mega = pandas.read_csv("mega.csv")
# pay_group = mega.groupby('p')
# coffee_group_by_pay = pay_group['cf'].value_counts()
# checkCard = coffee_group_by_pay['체크카드']
# plt.rcParams['font.family'] = 'Malgun Gothic'
# checkCard.plot.pie(autopct='%1.1f%%')
# plt.show()

# 아침에 20대 몇명 30대 몇명 40대 몇명
mega = pandas.read_csv("mega.csv")
time_group = mega.groupby('t')
coffee_group_by_age = time_group['a'].value_counts()
morning = coffee_group_by_age['아침']
plt.rcParams['font.family'] = 'Malgun Gothic'
morning.plot.pie(autopct='%1.1f%%')
plt.show()