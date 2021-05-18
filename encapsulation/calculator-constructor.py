 Calculator:

    def __init__(self, first, second): # 서브루틴이 되려면 리턴이 존재하면 안된다.
        self.first = first
        self.second = second

    def add(self):
        return c.first + c.second

    def sub(self):
        return c.first - c.second

    def mul(self):
        return c.first * c.second

    def div(self):
        return c.first / c.second


if __name__ == '__main__':
    c = Calculator(1, 2)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())