# alp = input("알파벳 하나만 입력해보세요")
# if alp.isupper():
#     print(alp.lower())
# elif alp.islower():
#     print(alp.upper())
# else:
#     print("너 내가 시킨대로 안했지")
#
# password = input("설정할 비밀번호를 입력하세요")
# if len(password) < 10:
#     print("최소 10글자")
# elif not ("!" or "@" or "#" in password):
#     print("특수문자 써주셈")
# elif password[0].islower():
#     print("첫번째는 대문자로")
# else:print("통과")

train = {
    "시내버스":1200,
    "광역버스":2000,
    "마을버스":1000,
}

user = input(f"{train}중 이용할 노선을 입력하세요")
age = int(input("나이를 입력하세요"))

if age <= 7:
    print(f"요금은 무료")
elif 8 <= age <= 19:
    print(f"요금은 {int(train[user]*0.7)}원")
elif age >= 65:
    print(f"요금은 무료")
else:
    print(f"요금은 {train}원")











