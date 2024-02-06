#data_structure
# int,float,str,list,bool,data_structure[list,

starbucks = {"아메리카노", "라떼", "프라푸치노", "샌드위치", "베이글"}
subway = {"샐러드", "샌드위치", "아메리카노", "랩", "쿠키"}

all_menu = starbucks.union(subway) # 합집합
inter_menu = starbucks.intersection(subway) #교집합
pureStarbucksMenu = starbucks.difference(subway) # 차집합
pureSubwayMenu = subway.difference(starbucks)
no_inter_menu = starbucks.symmetric_difference(subway) # 신문 데이터 분석..
print(no_inter_menu)














