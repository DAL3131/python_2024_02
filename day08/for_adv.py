fruits = ["apole", "bonano", "bluebell", "watermelong"]

#enumerate(): 번째, 요소 출력
#for i,j in enumerate(fruits):
#    print(f"{i}번째 {j}")
for i, j in enumerate(fruits):
    if j.count('a') == 0:
        print(i)

# 리스트 컴프리헨션
# [i for i in range()]
print([i for i in range(11)])

a = [i + 10 for i in range(11)]
print(a)

b = [i**2 for i in range(11)]
print(b)
fruits = ["apole", "bonano", "bluebell", "watermelong"]
print([i.upper() for i in fruits])












