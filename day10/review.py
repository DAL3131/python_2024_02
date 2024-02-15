# words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
# print([i for i in words if len(i)>5 and "a" in i])
#
# numbers = [30, 55, 20, 75, 40, 90 , 10, 65]
# over_fifty = [i for i in numbers if i > 50]
# print(over_fifty)

names = ["name", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]
people = [j for i, j in enumerate(names) if i%5 == 0]

print(people)






