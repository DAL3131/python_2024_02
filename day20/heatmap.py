import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas

mega = pandas.read_csv('mega.csv')
# size 나이와 커피의 크기 측정 함수
# unstack 행렬화 시키는 함수
table = mega.groupby(['p', 'cf']).size().unstack(fill_value=0)
plt.rcParams['font.family'] = 'Malgun Gothic'
sns.heatmap(table, cmap='coolwarm')
plt.show()


