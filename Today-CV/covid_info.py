from urllib import request
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime

target = request.urlopen("http://ncov.mohw.go.kr/")

soup = BeautifulSoup(target, "html.parser")

class Function:
  def __init__(self):
    self.num = 0
    print("코로나 바이러스 감염증 정보 안내")
    self.hello()

  def hello(self):
    print("1. 예방 수칙 보기")
    print("2. 일일 확진자 수 보기")
    print("3. 누적 확진율 보기")
    print("4. 자가진단 하기")
    print("5. 종료")

    self.num = int(input("이용하실 기능을 선택해주세요.(1~5) >>> "))

  def num_1(self):
    with open('예방 수칙.txt', 'r', encoding='UTF8') as file:
      for line in file:
        print(line.strip('\n'))
    
    self.hello()
    
  def num_2(self):
    self.nums = []
    for item in soup.select("div.datalist"):
      for data in item.select("span.data"):
        self.nums.append(int(data.string))

    print("현재까지 오늘 코로나 확진자 수는 ", sum(self.nums), "명입니다.")

    self.hello()

  def num_3(self):
    for item in soup.select("div.info_core"):
      for data in item.select("span.num"):
        self.percent = data.string

    print("현재까지 계산된 누적 확진율은 ", self.percent, "입니다.")

    self.hello()
    
  def num_4(self):
    self.name = str(input('이름을 입력하세요. >>> '))
    print('다음 질문에 대하여 예, 아니오로 입력해주세요.')
    self.chk_1 = str(input('1. 학생 본인이 코로나19가 의심되는 아래의 임상증상*이 있나요? * (주요 임상증상) 체온 37.5℃ 이상, 기침, 호흡곤란, 오한, 근육통, 두통, 인후통,후각·미각 소실 또는 폐렴. * (단, 코로나19와 관계없이 평소의 기저질환으로 인한 증상인 경우는 제외) >>> '))
    self.chk_2 = str(input('2. 학생 본인 또는 동거인이 코로나19 의심증상으로 진단검사를 받고 그 결과를 기다리고 있나요? >>> '))
    self.chk_3 = str(input('3. 학생 본인 또는 동거인이 방역당국에 의해 현재 자가격리가 이루어지고 있나요? ※ <방역당국 지침> 최근 14일 이내 해외 입국자, 확진자와 접촉자 등은 자가격리 조치 단, 직업특성상 잦은 해외 입·출국으로 의심증상이 없는 경우 자가격리 면제 >>> '))
    if self.chk_1 == self.chk_2 == self.chk_3 == "아니오":
      self.result = "의심 증상 없음"
      print('코로나19 예방을 위한 자가진단 설문결과 의심 증상에 해당되는 항목이 없어 출근 및 등교가 가능함을 알려드립니다.')
    else:
      self.result = "자가격리 필요"
      print('현재 건강상태는 가정 내에서 보호가 필요한 상태이므로 건강한 생활을 위해 잠시 출근 및 등교하지 않도록 협조하여 주시기 바랍니다.')

    self.now = datetime.now()

    self.nowDate = self.now.strftime('%Y-%m-%d')
    self.nowTime = self.now.strftime('%H:%M')

    self.excel_save(self.nowDate, self.nowTime, self.name, self.result)

    self.hello()

  def excel_save(self, nowDate, nowTime, name, result):
    wb = openpyxl.load_workbook('코로나 현황.xlsx')
    sheet = wb.active
    sheet.append([nowDate, nowTime, name, result])
    wb.save("코로나 현황.xlsx")

  def num_5(self):
    print("프로그램이 종료됩니다. 감사합니다.")
    quit()

user = Function()

while True:
  if user.num == 1:
    user.num_1()
  elif user.num == 2:
    user.num_2()
  elif user.num == 3:
    user.num_3()
  elif user.num == 4:
    user.num_4()
  elif user.num == 5:
    user.num_5()
