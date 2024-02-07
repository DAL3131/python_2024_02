#
# > 사전(Dictionary, 줄여서 'dict'는 키(key)와 값(value)의 쌍으로 이루어진 자료구조입니다.
# >
# > 사전은 키를 통해 빠르게 값을 찾을 수 있으며, 키는 각각 고유해야 합니다.
# >
# > 사전은 마치 실제 사전처럼, 단어(키)와 그에 해당하는 정의(값)의 쌍으로 데이터를 저장합니다.
#
# ### 사전의 기본
# my_dict = {'name': 'Alice', 'age': 25}
# print(my_dict['name']) #'Alice' 연산자
# print(my_dict.get['name']) #'Alice' 기능
# print(my_dict.get['gender', 'Not Spectified']) #'Not Spectified' (기본값 사용)
#
# my_dict = {'name': 'Bob', 'age' : '30', 'job' : 'developer'}
# #keys
# print(list(my_dict.keys())) # ['name', 'age', 'job']
# print(list(my_dict.values())) # ['bob', '30', 'developer']
# print(list(my_dict.items())) # [('name', 'bob'), ('age', '30'), ('job', 'developer')]
#
#
# # 제어문(Control Statements)
# >프로그램의 흐름을 제어하는 데 사용되는 구문들을 말합니다
# >
# >기본적으로 프로그램은 위에서 아래로 순차적으로 명령을 실행하지만, 제어문을 사용하면
# >특정 조건에 따라 코드의 실행 순서를 변경하거나 반복할 수 있습니다.
# >
# >주요 제어문에는 조건문과 반복문이 있습니다.
#
# 1. 조건문(Conditional Statements)
# a. if, dict
# 2. 반복문(Looping Statements)
# a. for, while


# if 조건
# num = int(input("정수 입력:"))

# if num > 0:
#     print("양수입니다"),
# print('나가')

#text = input("문자 입력하세요:")

#if len(text) >= 10:
#    print("너무 길어요!")
#if len(text) < 10:
#    print("끝")

#text = input("문자 입력하세요:")

#if len(text) >= 5 and text[-1].isupper():
#    print('통과')

#num = int(input("정수입력하세요:"))
#if num > 0:
#    print("양수입니다.")
#else:
#    print("음수 또는 0 입니다.")
#print("나가")

#num = int(input("수를 입력:"))
#if num % 2 == 1:
#    print("홀수임")
#else:
#    print("짝수임")

#alp = input("알파벳들을 입력:")
#if len(alp)%2 == 1:
#    print("길이가 홀수임")
#else:
#    print("길이가 짝수임")

#alph = input("알파벳 하나만 입력:")
#if alph.isupper():
#    print('대문자임')
#else:
#    print('소문자임')

# num = int(input("정수 입력:"))
# if num > 0:
#     print('정수')
# elif num == 0 :
#     print('0')
# else:
#     print('음수')

# score = int(input("수학 점수:"))
#
# if score >= 90:
#     print('a')
# elif score >= 80:
#     print('b')
# elif score >= 70:
#     print('c')
# else:
#     print("🤣샷건각")

# angle = int(input("0~180도 사이 각을 입력"))
# if angle < 90:
#     print("예각")
# elif angle == 90:
#     print('직각')
# elif angle == 180:
#     print('평각')
# elif angle > 90 and angle < 180:
#     print('둔각')
# else:
#     print('나가 인마')

#중첩 if문
# if True:
#     if True:
#         print('실행')
#     else:
#         print('나가')

word = input('단어 입력:')
if len(word)%2 == 0:
    if 'a' in word: #if word.count(a) > 0:
        print('a를 포함한 짝수네요')
    else:
        print('그냥 짝수네요')
elif len(word)%2 == 1:
    if 'a' in word:
        print('a를 포함한 홀수네요')
    else:
        print('그냥 홀수네요')



















#https://velog.io/@ubin_ing/data-analysis-relationship-youandme
