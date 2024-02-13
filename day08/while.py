# 반복문: for, while

# a = 1
# while a < 5:
#     print("아이고난")
#     a += 1

# while True:
#     num = int(input("정수 0을 넣으면 끝남"))
#     if num == 0:
#         break

# while문을 사용해서 1부터 10까지 더한 값을 출력
# a = 1
# total = 0
# while a < 11:
#     print(a)
#     total += a
#     a += 1
# print(total)

# 유저에게 어떤 정수 n를 입력 받고,
# while 무한루프에서 정수 n을 입력받으면 탈출하는 코드 만들기

# n = int(input("정수 입력:"))
# while True:
#     num = int(input("정수 입력:"))
#     if num == n:
#         break

# 랜덤으로 0~10까지 아무 숫자를 뽑고
# 유저에게 해당 숫자를 맞추게 하는 게임
# 맞추면 정답입니다 하고 끝
# 틀리면 틀렸습니다. 다시 입력하세요.

import random
n = random.randint(0, 11)

while True:
    m = int(input("뭘까요"))
    if m == n:
        print("정답입니다")
        break
    elif m != n:
        print("틀렸습니다. 다시 입력하세요")





















