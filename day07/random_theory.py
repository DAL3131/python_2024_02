import random

# randint(start, end): 임의의 정수 뽑기
print(random.randint(0, 10)) # 0~10 사이의 정수를 뽑기

# choice([]): 리스트에서 임의로 뽑기
print(random.choice(['엄마는 외계인','뉴욕치즈','민초']))

# random(): 0과 1사이의 실수
print(random.random())

# shuffle(): 리스트를 섞기
a =[1,2,3,4,5]
random.shuffle(a)
print(a)































