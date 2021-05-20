import random

class Account(object):
    def __init__(self, name, number, balence):
        self.bank = 'sc은행'
        self.name = name
        self.number = number
        self.balence = balence

    def get_account(self):
        return f'은행{self.bank},이름{self.name},계좌번호{self.number},잔액{self.balence}'


    @staticmethod
    def main():

        while 1:
            menu = input('0.종료, 1.입력, 2.출력')
            if menu == '0':
                print('프로그램을 종료합니다.')
                break
            elif menu =='1':
                a = Account(input('은행'),input('이름'),input('계좌번호'),input('잔액'))
            elif menu =='2':
                print(f'출력결과:{a.get_account}')
            else:
                print('숫자를 다시 입력하세요')
                continue

Account.main()
