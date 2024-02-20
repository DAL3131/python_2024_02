# Circle 클래스 만들기

class Circle:
    def __init__(self, 반지름):
        self.반지름 = 반지름

    def 원넓이(self, 반지름):
        return (반지름**2) * 3.14
    def 원둘레(self, 반지름):
        return 반지름*2 * 3.14
a = Circle(12)
print(a.원넓이(12))































