class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self): # getter는 파라미터가 존재하지 않기때문에 쉼표이후가 들어가면 안된다.
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def get_grade(self):
        score = int(self.avg())
        grade = ''
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'B학점'
        elif score >= 70:
            grade = 'C학점'
        elif score >= 60:
            grade = 'D학점'
        else:
            grade = 'F학점'

        return grade

    @staticmethod
    def main():
        g = Grade(int(input('국어점수')), int(input('영어점수')), int(input('수학점수')))
        print(f'총점:{g.sum()}')
        print(f'평균:{g.avg()}')
        print(f'학점:{g.get_grade()}')

Grade.main()

