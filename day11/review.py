# def minus(x, y):
#     return x-y
# c = minus(1, 3)
# print(c)

# def egg():
#     while True:
#         print("🥚")
# print(egg())

# def fry(x):
#     if x == "🥚":
#         return "🍳"
#     else:
#         return "??"
# print(fry(" "))

def zodiac(a):
    year = {
        0:"🐵",
        1:"🐔",
        2:"🐶",
        3:"🐷",
        4: "🐭",
        5: "🐮",
        6: "🐯",
        7: "🐰",
        8: "🐲",
        9: "🐍",
        10: "🐴",
        11: "🐑",
    }
    return year[a%12]

print(zodiac(2010))









































