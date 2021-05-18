class Grade:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3


if __name__ == '__main__':
    g = Grade(70, 90, 77)
    print(g.sum())
    print(g.avg())
