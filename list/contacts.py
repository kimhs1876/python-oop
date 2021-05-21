class Contacts(object):
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def get_contacts(self):
        return f'주소록: 이름 {self.name}, 전화번호 {self.phone}, 이메일 {self.email}, 주소 {self.addr}'


    @staticmethod
    def del_element(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

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
                edit_name = input('이름을 입력하세요: ')
                edit_info = Contacts(input('수정 전화번호'), input('수정 이메일'), input('수정 주소'), edit_name)
                edit_name.del_element(ls, name)
                ls.append(edit_info)

            elif menu == '4':
                del_name = input(ls, '삭제할 이름 :')
                edit_name.del_element(ls, name.)

            else:
                print('숫자를 다시 입력하세요')
                continue



Contacts.main()



