#str_adv
# num, str, bool, list
# 문자열 연산자
# +: 연결 연산자
# *: 반복 연산자
# "ice"[0] => "i": 인덱싱 연산자
# "armericano"[0:5]: 슬라이싱 연산자
# in: "ice" in "icearmericano": in 연산자

# print(), input(), int(), str(), bool(), list()
# len() # 길이 구해줌 [문자] 문자길이 [리스트] 요소갯수
# a = len("adssfasdffasdf")

a = "megastudy".replace("mega", "mini")
print(a)
b = "사과, 바나나, 체리".split(",") #문자 -> 리스트 /
print(b)
c = list("아메리카노")
print(c)
d = "사과, 바나나, 체리".split(", ")
print(d)
e = ", ".join(['🍎','🍒','c','d','e']) # join은 리스트 -> 문자열
print(e)
# 유저한테 문자를 입력을 받고
# 단어 사이에 !를 넣는 프로그램 만들기

text = input("문자를 입력:")
result = "!".join(list(text))
print(result)
# dd = "!".join(text)
# print(dd)

# is ~~ 니?
"abcdef".isdigit() #숫자니?
"bcdefg".isalnum() #숫자 or 문자이니?
"cdefgh".islower() #소문자니?
"defghi".isupper() #대문자니?





















