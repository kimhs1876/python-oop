class Bmi_Calculator:
    pass
    def setdata(self, weight, height):
        self.weight = weight
        self.height = height
    def bmi(self):
        return b.weight / (b.height * b.height)


if __name__ == '__main__':
    b = Bmi_Calculator()
    b.setdata(97, 1.87)
    print(b.bmi())