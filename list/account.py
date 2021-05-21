import random
class Account(object):
    def __init__(self, name, account_num, money):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_num = account_num
        self.money = money
    def to_string(self):
        return(f'Bank Name : {self.BANK_NAME}, Name : {self.name}, Account Number : {self.account_num}, Balance : {self.balance}')
    @staticmethod
    def create_account_num():
        ls = [str(random.randint(0,9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append((str(random.randint(0,9))))
        return "".join(ls)
    @staticmethod
    def del_account(ls, account_num):
        for i,j in enumerate(ls):
            if j.account_num == account_num:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료, 1.계좌개설, 2.계좌조회, 3.입금, 4.출금 5.계좌탈퇴')
            if menu == '0':
                print("프로그램을 종료합니다.")
                break
            elif menu == '1':
                ls.append(Account(Account.create_account_num(), input('name'), input('money')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                account_num = input('입금할 계좌번호')
                money = input('입금액 입력바랍니다.')
                for i, j in enumerate(ls):
                    if j.account_num == account_num:
                        replace = Account(j.account_num, j.name, int(j.money) + int(money)) # 입금 +
                        Account.del_account((ls, account_num))
                        ls.append((replace))
            elif menu == '4':
                account_num = input('출금할 계좌번호')
                money = input('출금액 입력바랍니다.')
                for i, j in enumerate(ls):
                    if j.account_num == account_num:
                        replace = Account(j.account_num,j.name, int(j.money) - int(money))
                        Account.del_account(ls, account_num)
                        ls.append((replace))
            elif menu == '5':
                Account.del_account(ls, input('삭제할 계좌번호'))
            else:
                print("숫자를 다시 입력하세요")
                continue
Account.main()