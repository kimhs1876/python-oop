class Contacts(object):
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def get_contact(self):
        return f'이름{self.name},핸드폰{self.phone},이메일{self.email},주소{self.addr}'

    @staticmethod
    def del_name(list, name):
        for i, j in enumerate(list):
            if j.name == name:
                del list[i]

    @staticmethod
    def main():
        list = []
    while 1:
        menu = input('0.종료 1.생성 2.조회 3.수정 4.삭제')
        if menu == '0':
            print('프로그램을 종료합니다.')
            break
        elif menu == '1':
            list.append(Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))) # Contacts의 에러 발생원인을 모르겠음
        elif menu == '2':
            for i in list:
                print(f'출력결과 : {i.get_contact()}')
        elif menu == '3':
            name = input('이름')
            del_name = input('삭제할 이름:')
            edit_info.del_name(list, name)
        elif menu == '4':
            edit_name = input('수정할 이름:')
            edit_info = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
            edit_info.del_name(list, name)
            list.append(edit_info)
        else:
            print('숫자를 다시 입력하세요')
            continue

Contacts.main()
