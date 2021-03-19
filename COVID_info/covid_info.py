from urllib import request
from bs4 import BeautifulSoup

print("코로나 바이러스 감염증 정보 안내")
print("1. 예방 수칙 보기")
print("2. 일일 확진자 수 보기")
print("3. 지역별 거리두기 단계 현황")
print("4. 자가격리 규칙")
print("5. 거리두기 단계별 규칙")
print("6. 종료")

num = int(input("이용하실 기능을 선택해주세요.(1~5) >>> "))

target = request.urlopen("http://ncov.mohw.go.kr/")

soup = BeautifulSoup(target, "html.parser")

nums = []

for item in soup.select("div.datalist"):
  for data in item.select("span.data"):
    nums.append(int(data.string))

if num == 1:
  pass
elif num == 2:
  print("현재까지 오늘 코로나 확진자 수는 ", sum(nums), "명입니다.")
elif num == 3:
  pass
elif num == 4:
  pass
elif num == 5:
  pass
elif num == 6:
  print("프로그램이 종료됩니다. 감사합니다.")
  quit()
