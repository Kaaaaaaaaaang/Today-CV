from urllib import request
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime

print("코로나 바이러스 감염증 정보 안내")
print("1. 예방 수칙 보기")
print("2. 일일 확진자 수 보기")
print("3. 누적 확진율 보기")
print("4. 자가진단 하기")
print("5. 종료")

num = int(input("이용하실 기능을 선택해주세요.(1~5) >>> "))

target = request.urlopen("http://ncov.mohw.go.kr/")

soup = BeautifulSoup(target, "html.parser")

nums = []

for item in soup.select("div.datalist"):
  for data in item.select("span.data"):
    nums.append(int(data.string))

for item in soup.select("div.info_core"):
  for data in item.select("span.num"):
    percent = data.string

if num == 1:
  with open('예방 수칙.txt', 'r', encoding='UTF8') as file:
    for line in file:
      print(line.strip('\n'))
elif num == 2:
  print("현재까지 오늘 코로나 확진자 수는 ", sum(nums), "명입니다.")
elif num == 3:
  print("현재까지 계산된 누적 확진율은 ", percent, "입니다.")
elif num == 4:
  name = str(input('이름을 입력하세요. >>> '))
  print('다음 질문에 대하여 예, 아니오로 입력해주세요.')
  chk_1 = str(input('1. 학생 본인이 코로나19가 의심되는 아래의 임상증상*이 있나요? * (주요 임상증상) 체온 37.5℃ 이상, 기침, 호흡곤란, 오한, 근육통, 두통, 인후통,후각·미각 소실 또는 폐렴. * (단, 코로나19와 관계없이 평소의 기저질환으로 인한 증상인 경우는 제외) >>> '))
  chk_2 = str(input('2. 학생 본인 또는 동거인이 코로나19 의심증상으로 진단검사를 받고 그 결과를 기다리고 있나요? >>> '))
  chk_3 = str(input('3. 학생 본인 또는 동거인이 방역당국에 의해 현재 자가격리가 이루어지고 있나요? ※ <방역당국 지침> 최근 14일 이내 해외 입국자, 확진자와 접촉자 등은 자가격리 조치 단, 직업특성상 잦은 해외 입·출국으로 의심증상이 없는 경우 자가격리 면제 >>> '))
  if chk_1 == chk_2 == chk_3 == "아니오":
    result = "의심 증상 없음"
    print('코로나19 예방을 위한 자가진단 설문결과 의심 증상에 해당되는 항목이 없어 출근 및 등교가 가능함을 알려드립니다.')
  else:
    result = "자가격리 필요"
    print('현재 건강상태는 가정 내에서 보호가 필요한 상태이므로 건강한 생활을 위해 잠시 출근 및 등교하지 않도록 협조하여 주시기 바랍니다.')

  now = datetime.now()

  nowDate = now.strftime('%Y-%m-%d')
  nowTime = now.strftime('%H:%M')

  wb = openpyxl.load_workbook('코로나 현황.xlsx')
  sheet = wb.active

  sheet.append([nowDate, nowTime, name, result])
  wb.save("코로나 현황.xlsx")
elif num == 5:
  print("프로그램이 종료됩니다. 감사합니다.")
  quit()