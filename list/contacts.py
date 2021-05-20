class Contacts(object):
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def get_contacts(self):
        return f'주소록: 이름 {self.name}, 전화번호 {self.phone}, 이메일 {self.email}, 주소 {self.addr}'




    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료, 1.입력, 2.출력 3.삭제')
            if menu == '0':
                print('종료........')
                break
            elif menu == '1':
                c = Contacts(input('이름'), input('전화번호'), input('이메일'),input('주소'))
                ls.append(c)

            elif menu == '2':
                for i in ls:
                    print(i.get_contacts())

            elif menu == '3':
                del_name = input('삭제할 이름 :')
                for i,j in enumerate(ls):
                    if i.name == del_name:
                        del ls[i]

    


            else:
                print('숫자를 다시 입력하세요')
                continue



Contacts.main()

