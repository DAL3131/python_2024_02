# 2호선별로 그룹핑
import pandas
subw = pandas.read_csv('subway.csv')
lines = subw.groupby('노선명')
station = lines['역명'].value_counts()

# 승차총승객수 그룹핑하고 역명 나타내기
user = subw.groupby('승차총승객수')
statio = user['역명'].value_counts()
print(statio)