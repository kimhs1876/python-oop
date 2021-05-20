class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_stockinfo(self):
        return f' 주식: 이름 {self.name}, 코드 {self.code}'

    @staticmethod
    def main():
        while 1:
            menu = input('0.종료, 1.입력, 2.출력')
            if menu == '0':
                print('프로그램을 종료합니다')
                break
            elif menu == '1':
                s = Stock(input('이름'), input('코드'))
            elif menu == '2':
                print(f'출력결과: {s.get_stockinfo()}')
            else:
                print('숫자를 다시 입력하세요')
                continue
Stock.main()