# 1. 기본식
# [i for i in range(100)]
# [1 for i in range(100)]
# [표현식 for 항목 in 반복가능객체(리스트,문자열,range...)]
# a = [i for i in "chocolate"]
# b = [i+10 for i in[1,2,3]]

# 2. 조건문(filter)
# print([i for i in range (100) if i%2==0])
# print([i for i in range(10000) if i%15==0])

cholist = ["Ghana", "Godiva", "Hershey", "Royce"]
# [5, 6, 7, 5]
# print([len(i) for i in cholist])
# print([i for i in cholist if len(i)%2==0])
# print([i for i in cholist if "e" in i])

# 3. 조건문(치환)
# print([i if i%2 == 0 else '💛' for i in range(101)])
# print(['👏'  if i%3 == 0 else i for i in range(101)])
# print(['🍫' if 'a' in i else len(i) for i in cholist ])


# 369게임
# 1~100 출력하는데, 3,6,9가 포함되어있으면 '👏', 없으면그대로

# print(['👏' if str(i%10) in '369' or str(i // 10) in '369' else i for i in range(1, 101)])



# 4. 중첩 루트 컴프리헨션

# print([(i, j) for i in range(10) for j in range(10)])
print(f"{i}*{j}={i*j}"[i*j for i in range(1, 10) for j in range(1, 10)])
# a = [i for i in range(1, 10)]
# b = [j for j in range(1, 10)]
# print(a)






































































































