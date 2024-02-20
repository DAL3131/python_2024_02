# 구조체 + 함수 = 클래스(설계도)
class Student:
    def __init__(self,a,b):
        self.name = a
        self.age = b
        self.courses = []

    # 함수 영역
    def introduce(self):
        print(f"{self.name}의 나이는 {self.age} 등록된 강의:{self.courses}입니다.")
    def enroll(self,a):
        self.courses.append(a)
        print(f"{a}강의가 등록되었습니다.")



# lee = Student("이연우",21)
# kwon = Student('권성혁',15)
# kim = Student('김태양',15)
# ahn = Student('안지우',21)
#
# lee.enroll("자료구조개론")
# lee.enroll('세계 리더십')
# ahn.enroll("이산구조")
# ahn.enroll('선형대수')
# kwon.enroll("도덕")
# kwon.enroll("기술가정")
# kim.enroll("보건")
# kim.enroll("체육")
#
# lee.introduce()
# ahn.introduce()
# kwon.introduce()
# kim.introduce()


# studentList = []
#
# while True:
#     systemNumber = int(input('1. 학생 등록 2. 해당 학생 과목 등록 3.해당 학생 과목 보기:'))
#     if systemNumber == 1:
#         name = input('이름 입력:')
#         age = int(input('나이 입력:'))
#         studentList.append(Student(name,age))
#         print(f"{name} 학생 등록 완료!")
#     elif systemNumber == 2:
#         for i in studentList:
#             i.introduce()
#         studentNumber = int(input("번호 고르세요:"))
#         course = input("과목 넣기:")
#         studentList[studentNumber].enroll(course)
#     elif systemNumber == 3:
#         for i in studentList:
#             i.introduce()

class BankAcount:
    def __init__(self, accout, name):
        self.account = accout
        self.name = name
        self.balance = 0

    def deposit(self, a):
        self.balance + a
        print("입금이 완료되었습니다.")
    def whithdraw(self, a):
        if self.balance - a < 0:
            print("출금할 금액이 너무 큽니다.")
        else:
            self.balance -= a
            print("출금이 완료되었습니다.")
    def checkBalance(self):
        print(f'현재 잔액은 {self.balance}입니다.')



