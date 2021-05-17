class Grade:
    def setGrade(self, kor, eng, math): # 기계적으로 해줘야 한다.
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def sum(self):
        return self.sum() / 3


if __name__ == '__main__':
    g = Grade()
    g.setGrade(99, 70, 88)
    print(g.sum())
    print(g.avg())
