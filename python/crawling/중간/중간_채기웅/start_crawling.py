#파이썬 프로그래밍 원칙!!!
#1. 무조건 객체화, 캡슐화, 함수로만!
#2. 각 함수 및 클래스의 책임을 단일적으로만 정의하기!!
#★3. 전역변수의 사용을 최소화해!!!! 그냥 사용하지 마 사용하지마 사용절대 하지마  

from bs4 import BeautifulSoup#pip로 설치필요
import time
import datetime
from datetime import date, timedelta
import requests #pip로 설치필요
#pandas 관련 모듈
import pandas as pd#pip로 설치필요
import numpy as np#pip로 설치필요

#시스템 관련 모듈
import os

from tendo import singleton #프로그램 중복 실행 방지 모듈 #pip로 설치 요
me = singleton.SingleInstance()#프로그램 중복 실행 방지 

def stock_check(url): #iherb의 stock check
    try:#*1피드백 반영
        response = requests.get(url)
        #print(response.headers)#웹사이트의 헤더 정보를 표시한다.
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find("h1",{"itemprop":"name", "id":"name"}).get_text()# 상품 제목 태그
        stock_status=soup.find("div",{"id":"stock-status"}).contents[1].get_text(strip=True).replace("\n","").replace("  ","") #첫번째 있는 것이 실제 품절/재고 있음이 있는 태그

        if str(stock_status) == "재고있음":
            stock_status = "재고있음"
        elif str(stock_status) == "품절":
            stock_status = "품절"
        else:
            stock_status = "오류발생"

        now=datetime.datetime.now()
        nowstr=now.strftime('%m/%d %H:%M')
        return [title, stock_status, nowstr] #0:title, 1:stock_status, 2:nowstr
    except Exception as e:
        print("오류로 인해 크롤링이 정상적으로 완료되지 않았습니다.\n 오류코드:\n "+str(e))
        print("프로그램 종료")
        return exit()

def save_to_csv(df_stocks, save_dir, save_name): #적절한 판단으로 csv로 저장하는 함수 (사실상 store_csv의 일부로 작동하는 미니함수라고 봐야됨.)
    #왜 df_stocks까지 넣느냐?
    #캡슐화하고 전역변수의 사용을 최소화 하려고!
    save_file=save_dir+save_name+".csv"
    print(save_file)
    #-------원 데이터를 csv로 저장---------
    try:
        if os.path.isfile(save_file): 
            df_stocks.to_csv(save_file, mode='a', header=False, encoding="utf-8-sig", index=False)#a는 원본에 데이터를 추가해서 저장하겠다는 뜻
        else: #동일한 파일이 없다면
            df_stocks.to_csv(save_file, mode='a', header=True, encoding="utf-8-sig", index=False)#utf-8-sig인코딩을 사용하면 한글도 깨지지 않음
        return True #정상 저장되었다면 True 
    except Exception as e: #만약 사용자가 파일을 열어보고 있거나 오류가 발생하면
        print("save_to_csv Error :\n", e)
        return False #비정상이면 False

# 데이터 저장 및 "업데이트(쌓아서 저장:store)"를 하는 함수이며 또한
# 만약 사용자가 csv_files내의 csv를 열어보고 있다면 임시로 추가 크롤링된 데이터를 dontouch 폴더내에 csv형식으로 저장한 다음
# 사용자가 csv열람을 끝냈을 때 임시저장한 크롤링 데이터를 csv_files내의 csv(원본)에 붙여넣고 임시파일은 삭제하는 함수이다.
def store_csv(df_stocks, save_dir, prefix_="[iherb-재고여부확인]", _suffix=""):
    #어제 오늘 날짜
    yesterday = str(date.today() - timedelta(1)) 
    today = str(date.today())

    #원본 업데이트 전 코어폴더에 쌓인 데이터가 있는지 확인하고 있다면 붙여쓰고 삭제하기
    #csv_today 경로
    path_csv_today = "./dontouch/" + today + _suffix + ".csv"

    if os.path.isfile(path_csv_today): #오늘 임시 저장 파일이 있다면
        print("csv_today 추가붙여쓰기 시작")
        csv_today = pd.read_csv(path_csv_today, encoding="utf-8-sig")
        is_saved = save_to_csv(csv_today, save_dir, prefix_ + today + _suffix)
        if is_saved:
            print("csv_today 추가붙여쓰기 완료")
            os.remove(path_csv_today)# 붙여쓰기 한 후 추가 저장된 데이터는 삭제하기
        else:
            print("csv_today 추가붙여쓰기 실패")
    else:
        print('csv_today 파일 감지되지 않음')

    #csv_yesterday 경로
    path_csv_yesterday = "./dontouch/" + yesterday + _suffix + ".csv"

    if os.path.isfile(path_csv_yesterday): #어제 임시 저장 파일이 있다면
        print("csv_yesterday 추가붙여쓰기 시작")
        csv_yesterday = pd.read_csv(path_csv_yesterday, encoding="utf-8-sig")
        is_saved = save_to_csv(csv_yesterday, save_dir, prefix_ + yesterday + _suffix)#정상 저장되었는지 True False가 들어가는 변수인 is_saved
        if is_saved:
            print("csv_yesterday 추가붙여쓰기 완료")
            os.remove(path_csv_yesterday)
        else:
            print("csv_yesterday 추가붙여쓰기 실패")
    else: 
        print('csv_yesterday 파일 감지되지 않음')
    
    #-------원 데이터 보호를 위해 복사본으로 저장---------
    print("adding new row on save_dest")#원본에 저장
    is_saved = save_to_csv(df_stocks, save_dir, prefix_ + today +_suffix) #정상 저장되었는지 True False가 들어가는 변수인 is_saved
    print("added new row on save_dest ")
    if not is_saved: #만약 저장중 에러가 발생했다면
        save_to_csv(df_stocks, "./dontouch/", today + _suffix) #코어(내부)폴더 내에 따로 데이터 임시로 저장해두기


def make_dir(directory): #디렉토리가 없을 시 만들어주는 함수
    if not os.path.isdir(directory):
        os.mkdir(directory)

def remove_file(file_dir):#파일이 있을 시 없애주는 함수
    if os.path.isfile(file_dir):
        os.remove(file_dir)

def open_urls():
    #메모장에 있는 url들이 유효한지 검사
    try:
        f = open("./urls.txt", "r", encoding="utf-8")
        urls = [url.replace("\n", "").replace(",", "") for url in f.readlines()] #readlines로 분리된 줄 별 내용에서 엔터랑 콤마 빼기
        print(urls)
        f.close()
        if len(urls) == 0:#아무것도 입력 안했으면 error raise
            raise Exception 
        for url in urls:
            stock_check(url)# stock_check함수를 잘 통과하는지 체크

    except Exception as e:
        print("오류 발생, 오류코드 :\n"+str(e))
        print("urls.txt"+"가 현재 실행파일의 경로 같이 있는지, url을 정확히 입력했는지 확인해주세요")
        print("예시)\n \
            https://www.example1.com/1\n \
            https://www.example2.com/2\n \
            https://www.example3.com/3\n")
        exit()
    return urls


#6/28 피드백
#샤딩(shading) (o) 날짜별로 파일 분할하는 것으로 해결
#수정권한 문제(△)
#날짜마다 쪼개서 저장하면 복사하는 비용이 적게 듦 (o) "
#제때 정상적으로 업로드 되었는지 확인하는 코드도 짤 것 -> cmd창의 로그를 통해 확인 가능..?
#사용자에게 업데이트 알림이 갈지에 대해 결정 (x)-> GUI를 따로 구현하거나 동적 html을 따로 만들지 않는한 csv파일 자체에서 변화 내용이 있다는 사실을 알리기는 어려워보임..
#네이밍 규칙을 통일할 것!!!(o) -> 대부분 기본자료형_고유네임_고유네임... 형식
#=>GuI 포기함.

#=====================================================================main====================================================================================
def main(): #main(시작)함수
    urls = open_urls()
    print(len(urls))
    #중요 파일 저장경로 및 csv파일 저장경로
    core_dir = "./dontouch/"
    csv_files_dir = "./csv_files/"
    #파일 디렉토리 만들기
    make_dir(core_dir)
    make_dir(csv_files_dir)

    f=open("./dontouch/process_option.txt","w")
    f.write("True")#실행할 때는 flag를 True로(그래야 무한루프를 계속 도니까)
    f.close()

    #혹시 처음 시작시 존재할지도 모르는 코어(프로그램 내부)폴더 내 잔여 데이터(임시 저장 데이터) 제거
    remove_file(core_dir + str(date.today()) + ".csv")
    remove_file(core_dir + str(date.today()-timedelta(1)) + ".csv")

    print("go to mainloop")
    #mainloop
    while True:
        start_time=time.time()
        #while문 control하는 부분
        print("read ./dontouch/process_option.txt")
        f = open("./dontouch/process_option.txt","r")
        flag = f.readline()# 첫번째 줄 읽기
        f.close()
        print("flag :", flag)
        if flag == "False": #탈출문
            break

        dic_stocks = {'time':[]}#*1피드백 반영
        for url in urls: #재고 확인
            title, stock_status, nowstr = stock_check(url) #list로 return되어도 각각 변수 순서대로 들어감
            dic_stocks[title]=[]#*1피드백 반영
            print("[{}의 재고 확인]".format(title))
            print(nowstr,">>>", stock_status)

            if url == urls[0]:
                dic_stocks['time'].append(nowstr)
            dic_stocks[title].append(stock_status)

        df_stocks = pd.DataFrame(dic_stocks)
        print("df_stocks")
        print(df_stocks)
        print("save_to_csv")
        store_csv(df_stocks, "./csv_files/")#csv를 저장 및 업데이트 하는 함수
        process_time=time.time() - start_time #한번 크롤링할 때까지 걸린 시간
        print("sleep for {} sec".format(60-process_time))
        time.sleep(60-process_time) #process_time을 빼주는 이유: 실행하느라 걸린 시간을 빼야 crawling interval이 일정하게 유지됨
    exit()

if __name__ == "__main__": #이 파일을 import가 아닌 실행했을 때 작동
    main()
