from bs4 import BeautifulSoup # ??기능을 가져온다
from urllib.request import urlopen # ??기능을 가져온다
class MelonMusic(object): # 클래스 정의
    url ='' # def init 과 동일, 프로퍼티 정의되어 있다.
    def __str__(self): # to_string과 동일
        return f'URL : {self.url}'
    @staticmethod
    def scrap(soup, x):
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": x})):
            count += 1
            print(f'{str()} RANGKING')
            print(f'{x} " {i.find("a").text}')


    @staticmethod
    def main():
        melon = MelonMusic() # 생성자 생성?
        while 1:
            menu = int(input('0.종료\n1.Input URL\n2.Get Ranking'))
            if menu == 0:
                print("프로그램을 종료합니다.")
                break
            elif menu == 1:
                melon.url = input('Input URL')
            elif menu == 2:
                print(f'Input URL is {melon}')
                melon.soup = BeautifulSoup(urlopen(melon.url), 'lxml')
                print('-----------ARTIST RANKING--------------')
                melon.scrap(x="artist")
                print('-----------TITLE RANKING--------------')
                melon.scrap(x="title")
            else:
                print('숫자를 다시 입력하세요')
                continue
MelonMusic.main()