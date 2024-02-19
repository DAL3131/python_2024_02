class Student:
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.course = c
    def introduce(self):
        print(f"안녕하세요 {self.name}입니다. 나이는 {self.age}, 수강목록: {self.course}입니다.")

ki = Student('기민서', 24,["c언어",'자바'])
lee = Student('이연우', 21,["운영체제이론",'사고와 비판'])
ahn = Student('안지우', 21,["인공지능개론",'미적분학'
                                  ''])

ki.introduce()
lee.introduce()
ahn.introduce()















