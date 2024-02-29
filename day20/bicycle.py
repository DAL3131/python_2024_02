import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# bicycle = pandas.read_csv('bicycle.csv', encoding='cp949')
#
#
# def dongDelete(row):
#     if row['시작_대여소명']:
#         place = row['시작_대여소명'].split('_')[0]
#         return place[0:2]
#
# bicycle['대여소명'] = bicycle.apply(dongDelete, axis=1)
# bicycle.to_csv('new.csv', index=False, encoding='utf-8-sig')

bicycle = pandas.read_csv('new.csv')
plt.hist(list(bicycle['대여소명'].values))
plt.show()
# plt.hist(bicycle['대여소명'].values)
# plt.show()











