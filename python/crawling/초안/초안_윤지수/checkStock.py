import requests
from bs4 import BeautifulSoup
import datetime
import csv

def checkStock(URL):
  # URL = "https://kr.iherb.com/pr/California-Gold-Nutrition-Omega-800-Pharmaceutical-Grade-Fish-Oil-80-EPA-DHA-Triglyceride-Form-1000-mg-90-Fish-Gelatin-Softgels/85180"
  # URL = "https://kr.iherb.com/pr/California-Gold-Nutrition-Omega-800-Pharmaceutical-Grade-Fish-Oil-80-EPA-DHA-1-000-mg-30-Fish-Gelatin-Softgels/82845"
  # URL = "https://kr.iherb.com/pr/California-Gold-Nutrition-LactoBif-Probiotics-30-Billion-CFU-60-Veggie-Capsules/64009?rec=iherbtest-home"

  #html가져오도록 request
  response = requests.get(URL) 
  result = [response.status_code]

  if response.status_code == 200:
    #response
    html = response.text
    #객체로 만들어줌
    soup = BeautifulSoup(html, 'html.parser') 
    
    #날짜, 시간
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M')
    #제품명
    title = soup.find("h1", attrs={"id":"name"}).get_text()
    
    #재고확인
    button = soup.select_one("button.btn-secondary") 
    if button is None:
      button = soup.select_one("button.btn-primary > strong")
    
    button_text = button.text.strip()
    if(button_text == "입고 알림"):
      result = [date, time, title, "재고 없음"]
    elif(button_text == "장바구니에 담기"):
      result = [date, time, title, "재고 있음"]
  else:
    return result
  
  return result

#csv파일로 저장
URL = input("url을 입력해주세요 : ")
filename = "test.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
data = checkStock(URL)
writer.writerow(data)