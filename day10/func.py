# 함수[function]: (마술 상자) [input[None] & output[None]]
# [내장함수 or 표준함수 or 파이썬함수] print(), input(), int(), str(), bool(), len(), sum(), enumerate(), zip()
# [문자열 함수] 'abcd'.upper(), 'abcd'.isUpper(), 'abcd'.count('a')...
# 10 -> 20, 5 -> 10, 3 -> 6, 7 -> 14 f(x) = x*2
# a = str(123)
# b = len("abcde")
# a = input()
# print(a)

# 함수 정의
# def add(ㅁㄴㅇㄹ, ㄴㅁㄴㄹㅇ):
#     c = ㅁㄴㅇㄹ+ㄴㅁㄴㄹㅇ
#     return c
# print(add(100, 200))
#
# def substract(ㅁ, ㅠ):
#     ㅊ = ㅁ-ㅠ
#     return ㅊ
#
# def multiply(a, b):
#     c = a*b
#     return c
# print(substract(6,7))
# print(multiply(12,7))

# '🥚'
# makeTofry
# def makeTofry(a):
#     if a != '🥚':
#         return('?')
#     else:
#         return('🍳')
# print(makeTofry("🥚"))

# def bank(a):
#     bankName = {
#         '농협은행':'넘예쁘네',
#         '기업은행':'귀엽네',
#         '국민은행':'고민해',
#         '신한은행':'신나네',
#     }
#     return bankName.get(a, "?")
# print(bank('국민은행'))

#    if a == '농협은행':
#        return '넘예쁘네'
#    elif a == '기업은행':
#        return '귀엽네'
#    elif a == '국민은행':
#       return '고민해'
#    elif a == '신한은행':
#        return '신나네'

# 가변 매개변수
# def makePizza(*topping):
#     print("피자 오지게 굽는중")
#     for i in topping:
#         print(f"추가되는 토핑:{i}")
# makePizza('치즈', '버섯', '올리브', '페퍼로니')

#zodiac 띠구하기
#def zodiac(*arg) [1996 ~ 2005]
#zodiac(1996, 2000, 2005) - 쥐, 용, 닭

#def zodiac(*year):
#    zodiacDict = {
#        1996 : '쥐',
#        1997: '소',
#        1998: '호랭',
#        1999: '토',
#        2000: '용',
#        2001: '뱀',
#        2002: '말',
#        2003: '양',
#        2005: '🍗',
#        2006: '개',
#
#    }
#    for i in year:
#        print(f"{zodiacDict[i]}")


#zodiac(1996, 1997, 2000, 2002, 2005, 2006, 1998)

# 자연수 n이 매개변수로 들어오면, 배열화시키고 반대로 나타내기
# 12345 -> [5,4,3,2,1]

def func(n):
    a = list(str(n)).reverse()
    b = a.reverse()
    return[int(i) for i in b]
print(func(213214141))

































































































































































































































































































































































































































































