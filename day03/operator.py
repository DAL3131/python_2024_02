# operator(연산자)
# 토큰[token]
# 😊산술 연산자: +,-,*,/,//,**,% [숫자] int float
# 😊연결 연산자: + [문자] str
# 😊반복 연산자: * [문자]
# print("너무 졸리다 커피땡긴다"*5)
# print(3*5)

# 😊비교 연산자: >,<, <=, >=, ==[같다], != [다르다]
# 비교 연산자의 결과 타입: bool
# print(f"10 > 5: {10 > 5}")
# print(f"10 < 5: {10 < 5}")
# print(f"10 >= 5: {10 >= 5}")
# print(f"10 <= 5: {10 <= 5}")
# print(f"10 == 5: {10 == 5}")
# print(f"10 != 5: {10 != 5}")

# 😊대입 연산자: =, +=, -=, /= ...
# name = "메가짱"
# num = 1
# num += 5
# num *= 40
# print(num)

# 😊논리 연산자 bool : and, or, not
# and [그리고, 교집합]: 모든 조건이 참인 경우만 True
# or [또는, 합집합]: 하나의 조건이 참이면 True
# not: bool 결과를 반대로
# print(10 > 5 and 5 > 1 and 1 == 0)
# print(3 > 5 or 4 > 5 or 5 == 5)
# print(not bool(""))

# print((5>3) and (7 > 3))
# print((5<=3))

# 😊멤버쉽 연산자 타켓팅[문자]: in 결과값[bool]

print("mega" in "megastudy")
print("mega" not in "megastudy")

# 😊그룹핑 연산자 ()
print(3 + 2 + 1 / 3)

# 😊슬라이싱 연산자 타켓팅[문자열]
# [start:end:step] step씩 건너뜀
print("megastudy"[0:5]) #megas
print("megastudy"[:5]) #megas
print("megastudy"[0:5:2]) #mgs
print("megastudy"[::2]) #mgsuy

# 😊인덱싱 연산자:[]
print("coffee"[1])
print(not(5 <=3) or not(3<=1))
>>>정리











