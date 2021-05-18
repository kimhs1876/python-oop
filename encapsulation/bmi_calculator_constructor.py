class Bmi(object):

   def __init__(self, weight, height):
      self.weight = weight
      self.height = height
      '''
      고도 비만 : 35 이상
      중(重)도 비만 (2단계 비만) : 30 - 34.9
      경도 비만 (1단계 비만) : 25 - 29.9
      과체중 : 23 - 24.9
      정상 : 18.5 - 22.9
      저체중 : 18.5 미만
      '''
      def get_bmi(self):
          bmi = ''
          index = self.weight / self.height ** 2 * 10000
      def get_bmigrade(self):

         if index >= 35:
            bmi ='고도 비만'
         if index >= 30:
            bmi = '중도 비만'
         if index >= 25:
            bmi ='경도 비만'
         if index >= 23:
            bmi ='과체중'
         if index >= 18.5:
            bmi ='정상'
         else:
            bmi = '저체중'
         return bmi

   @staticmethod
   def main():
      b = Bmi(int(input('몸무게를 입력하세요')), int(input('키를 입력하세요')))
      print(b.get_bmi())

Bmi.main()