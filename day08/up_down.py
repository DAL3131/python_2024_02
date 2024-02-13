# 유저에게 난이도 고르기 (쉬움, 보통, 어려움)
# 난이도에 따라서
# - 1 ) 쉬움 0~100, 보통 0~1000, 어려움 0~10000 랜덤 숫자 뽑기
# 유저가 입력한 정수보다 랜덤숫자가 높으면 down, 낮으면 up, 맞추면 정답!
# 기회는 총 6번

import random
n = random.randint(0, 101)
n2 = random.randint(0, 1001)
n3 = random.randint(0, 10001)
ch = 6

diff = input("난이도 선택 :: 쉬움, 보통, 어려움)")
# rann = {
#     1:random.randint(0, 101),
#     2:random.randint(0, 1001),
#     3:random.randint(0, 10001),
# }
if diff == "쉬움":
    while True:
        m = int(input("뭘까요"))
        if m == n:
            print("정답!")
            break
        elif ch == 0:
            print("game over")
            print(f"정답은 {n}!")
            break
        elif m < n:
            print("up!")
            ch -= 1
        elif m > n:
            print("down!")
            ch -= 1

if diff == "보통":
    while True:
        m = int(input("뭘까요"))
        if m == n2:
            print("정답!")
            break
        elif ch == 0:
            print("game over")
            print(f"정답은 {n2}!")
            break
        elif m < n2:
            print("up!")
            ch -= 1
        elif m > n2:
            print("down!")
            ch -= 1

if diff == "어려움":
    while True:
        m = int(input("뭘까요"))
        if m == n3:
            print("정답!")
            break
        elif ch == 0:
            print("game over")
            print(f"정답은 {n3}!")
            break
        elif m < n3:
            print("up!")
            ch -= 1
        elif m > n3:
            print("down!")
            ch -= 1






















