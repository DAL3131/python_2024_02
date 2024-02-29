import pandas

mega = pandas.read_csv('mega.csv')
def event(row):
    if row['a'] == 50 or row['a'] == 60:
        return "discout"
    else:
        return "except"
def TWST(row):
    if row['p'] == '티머니' and row['a'] == 20:
        return "discout"
    else:
        return "except"
mega['어르신 이벤트'] = mega.apply(event, axis=1)
mega['티머니쓰는20대'] = mega.apply(TWST, axis=1)
print(mega)
g = mega.groupby('p')
print(g['20살먹고티머니로결제하는나'].value_counts())